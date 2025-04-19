# Mental Health AI Chatbot with WhatsApp Integration

## Overview

This project is a **Mental Health AI Chatbot**, named MindCare, designed to offer structured emotional support and guidance through WhatsApp. It uses advanced generative AI and risk classification to address user concerns, providing personalized and empathetic responses. The integration with Twilio ensures seamless communication, while Flask powers the backend framework.

## Features

- **Generative AI Responses**: Provides thoughtful and emotionally aware replies using Google's Gemini AI model.
- **Risk Classification**: Classifies user messages for potential distress or high-risk situations.
- **WhatsApp Integration**: Chatbot accessible via WhatsApp using Twilio APIs.
- **Crisis Alerts**: Sends high-risk alerts to a designated phone number for immediate intervention.
- **Context-Aware Conversations**: Maintains memory of past interactions to deliver coherent and structured guidance.

## Technologies Used

- **Flask**: Backend server for handling user messages and interactions.
- **Twilio API**: For WhatsApp message integration and alert notifications.
- **Google Gemini AI**: For generating personalized conversational responses.
- **Custom Risk Model**: Used to classify risk levels in user messages.
- **Docker**: Simplifies deployment and containerization.

## Installation and Setup

### Prerequisites

- Python 3.8 or higher
- Twilio Account and credentials
- Google API key (for generative AI integration)
- Docker (optional, for deployment)

### Steps to Install

1. Clone this repository:
   ```bash
   git clone https://github.com/YourUsername/MindCare.git
   cd MindCare
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Add environment variables in a `.env` file:
   ```plaintext
   API_KEY=<Your Google API Key>
   TWILIO_ACCOUNT_SID=<Your Twilio Account SID>
   TWILIO_AUTH_TOKEN=<Your Twilio Auth Token>
   TWILIO_WHATSAPP_NUMBER=whatsapp:+14155238886
   MY_PHONE_NUMBER=whatsapp:+918688343125
   ```

4. Run the Flask app locally:
   ```bash
   python app.py
   ```

5. (Optional) To run using Docker:
   ```bash
   docker build -t mental-health-chatbot .
   docker run -p 5000:5000 mental-health-chatbot
   ```

## How It Works

1. **User Interaction**:
   - A user sends a message to the WhatsApp chatbot via the Twilio sandbox or approved number.

2. **Risk Classification**:
   - Each message is analyzed to determine risk level (e.g., low, medium, high).

3. **AI Response**:
   - Generative AI responds with empathetic and context-aware replies.

4. **Crisis Alerts**:
   - In case of high risk, an alert message is sent to a designated phone number.

5. **Memory Retention**:
   - The chatbot remembers past interactions to provide seamless and logical assistance.

## Files and Folders

- **app.py**: Main Flask application.
- **risk_classification.py**: Risk classification model implementation.
- **db.py**: Handles storage of past conversations.
- **requirements.txt**: Python dependencies.

## License

This project is licensed under the [MIT License](LICENSE).

---
