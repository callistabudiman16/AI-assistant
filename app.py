from flask import Flask, request, jsonify, render_template
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Configure the API key
api_key = 'AIzaSyC4ioUQI4FaleKIYojxIFHybg8zhDCpS8o'

genai.configure(api_key=api_key)

# Create the model
model = genai.GenerativeModel('gemini-2.5-flash')

def load_prompt_template():
    """Load the prompt template from file"""
    with open('prompt_template_test.txt', 'r', encoding='utf-8') as file:
        return file.read()

def generate_sample_question(category, role, product_domain, company):
    """Generate a sample interview question based on the parameters"""
    question_templates = {
        'Product Sense': f"Design a new feature for our {product_domain.lower()} platform that would increase user engagement. Walk me through your thought process using a structured framework.",
        'Execution': f"You need to launch a new {product_domain.lower()} feature in 3 months. How would you approach the planning, execution, and delivery? What are the key risks and how would you mitigate them?",
        'Leadership & Collaboration': f"You're leading a cross-functional team to build a {product_domain.lower()} product. How would you handle conflicting priorities between engineering, design, and business stakeholders?",
        'Analytical & Impact': f"Our {product_domain.lower()} metrics are declining. How would you analyze the problem, identify the root cause, and propose a data-driven solution?",
        'System Design': f"Design a scalable {product_domain.lower()} system that can handle 10 million daily active users. Walk me through your architecture decisions, data flow, and scalability considerations.",
        'Coding & Algorithms': f"Implement an efficient algorithm to solve a {product_domain.lower()} problem. Walk me through your approach, time/space complexity, and optimization strategies.",
        'Technical Architecture': f"Design the technical architecture for a {product_domain.lower()} application. How would you structure the codebase, choose technologies, and ensure maintainability?",
        'Problem Solving': f"A critical {product_domain.lower()} service is experiencing performance issues in production. How would you debug, identify the root cause, and implement a solution?",
        'Data Structures': f"Design an efficient data structure to handle {product_domain.lower()} data operations. What are the trade-offs and how would you optimize for different use cases?",
        'Database Design': f"Design a database schema for a {product_domain.lower()} application. How would you handle relationships, indexing, and performance optimization?",
        'API Design': f"Design RESTful APIs for a {product_domain.lower()} service. How would you handle authentication, rate limiting, versioning, and error handling?",
        'Security & Scalability': f"Design a secure and scalable {product_domain.lower()} system. How would you handle authentication, data protection, and performance at scale?",
        'Code Review & Testing': f"Review this {product_domain.lower()} code and suggest improvements. How would you ensure code quality, maintainability, and comprehensive testing?"
    }
    
    return question_templates.get(category, f"How would you approach a {product_domain.lower()} challenge as a {role} at {company}?")

def substitute_parameters(template, company, role, product_domain, duration_minutes, mission, values_csv, category):
    """Substitute parameters in the prompt template"""
    # Generate the sample question
    sample_question = generate_sample_question(category, role, product_domain, company)
    
    # Replace the placeholders in the template with the provided parameters
    updated_template = template.replace('Meta interview panel', f'{company} interview panel')
    updated_template = updated_template.replace('Project Manager', role)
    updated_template = updated_template.replace('Social media and digital communications', product_domain)
    updated_template = updated_template.replace('10 minutes.', f'{duration_minutes} minutes.')
    updated_template = updated_template.replace('build the future of human connection and the technology that makes it possible', mission)
    updated_template = updated_template.replace('give people a voice, build connection and community, serve everyone, keep people safe and protect privacy, promote economic opportunity', values_csv)
    updated_template = updated_template.replace('Product Sense', category)
    updated_template = updated_template.replace('Meta-tailored', f'{company}-tailored')
    updated_template = updated_template.replace('Meta/social-media metrics', f'{company}/social-media metrics')
    
    # Add the sample question to the prompt
    updated_template = f"Interview Question: {sample_question}\n\n{updated_template}"
    
    return updated_template

@app.route('/generate', methods=['POST'])
def generate_response():
    """Generate interview response based on provided parameters"""
    try:
        # Get parameters from request
        data = request.get_json()
        
        # Validate required parameters
        required_params = ['company', 'role', 'product_domain', 'duration_minutes', 'mission', 'values_csv', 'category']
        for param in required_params:
            if param not in data:
                return jsonify({'error': f'Missing required parameter: {param}'}), 400
        
        # Extract parameters
        company = data['company']
        role = data['role']
        product_domain = data['product_domain']
        duration_minutes = data['duration_minutes']
        mission = data['mission']
        values_csv = data['values_csv']
        category = data['category']
        
        # Validate category
        valid_categories = [
            "Product Sense", "Execution", "Leadership & Collaboration", "Analytical & Impact",
            "System Design", "Coding & Algorithms", "Technical Architecture", "Problem Solving",
            "Data Structures", "Database Design", "API Design", "Security & Scalability", "Code Review & Testing"
        ]
        if category not in valid_categories:
            return jsonify({'error': f'Invalid category. Must be one of: {valid_categories}'}), 400
        
        # Load and customize the prompt template
        prompt = substitute_parameters(
            load_prompt_template(),
            company, role, product_domain, duration_minutes, mission, values_csv, category
        )
        
        # Generate the sample question for the response
        sample_question = generate_sample_question(category, role, product_domain, company)
        
        # Generate response using Gemini
        response = model.generate_content(prompt)
        
        # Return the response
        return jsonify({
            'success': True,
            'response': response.text,
            'question': sample_question
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/')
def index():
    """Serve the main web interface"""
    return render_template('index.html')

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({'status': 'healthy', 'message': 'API is running'})

if __name__ == '__main__':
    print("Starting Flask API server...")
    print("Available endpoints:")
    print("  GET / - Web interface")
    print("  POST /generate - Generate interview response")
    print("  GET /health - Health check")
    print("\n🌐 Web interface available at: http://localhost:5000")
    app.run(debug=True, host='0.0.0.0', port=5000)
