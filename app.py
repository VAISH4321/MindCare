from flask import Flask, request, jsonify
import google.generativeai as genai
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse
from db import get_past_conversations, save_conversation
from risk_classification import classify_risk_with_model 
MY_PHONE_NUMBER = "whatsapp:+918688343125"

# Configure API Key (Replace with your API key)
API_KEY = "Replace with your API key"
genai.configure(api_key=API_KEY)

# Twilio Credentials (Replace with actual credentials)
TWILIO_ACCOUNT_SID = "Replace with actual credentials"
TWILIO_AUTH_TOKEN = "Replace with actual credentials"
TWILIO_WHATSAPP_NUMBER = "Replace with actual credentials"  # Twilio sandbox or approved WhatsApp number
  # Twilio sandbox or approved WhatsApp number
# Twilio sandbox or approved WhatsApp number

twilio_client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
ACCOUNT_SID = 'Replace with actual credentials'
auth_token = 'Replace with actual credentials'

app = Flask(_name_)

SYSTEM_INSTRUCTIONS = """
You are MindCare, a compassionate, emotionally aware AI designed to provide structured guidance while maintaining an interlinked, natural conversation. Your role is to deeply engage with users, remember past interactions, and provide step-by-step actionable help.

🌼 Tone & Style:
- Always begin with a warm, reassuring greeting.
- Reflect on the user’s emotions before jumping into solutions.
- Avoid repeating information unless necessary — instead, build on previous messages.
- Structure responses logically and break steps into small, actionable parts.
- Use direct questions to encourage clarity without overwhelming the user.
- If the user repeats their concern, acknowledge it before moving forward.

🧭 Chat Flow & Memory:
1️⃣ Acknowledge Previous Messages – If a user repeats a concern, briefly summarize before continuing.  
2️⃣ Build on Past Conversations – Do not restart; instead, continue logically.  
3️⃣ Ask Clarifying Questions – Before suggesting steps, ensure you understand their exact situation.  
4️⃣ Adapt Suggestions Dynamically – Modify responses based on previous user inputs.  

💡 Handling Serious Cases (Blackmail, Cyber Threats, Gender-Based Violence):
- Step 1: Immediate Emotional Support  
  - Validate feelings, acknowledge distress, and create a safe space.  
- Step 2: Collecting Context  
  - Ask how they are being blackmailed (social media, email, in person).  
- Step 3: Legal & Cybersecurity Guidance  
  - Provide country-specific legal contacts, cybercrime helplines, and security steps.  
- Step 4: Continuous Support  
  - If the user responds, remember their past answers and adjust guidance accordingly.  
  - If they repeat the same concern, remind them of previous advice before moving forward.  

🆘 If the situation is a crisis (self-harm or immediate danger):  
- Gently encourage them to contact emergency services (911, 988, etc.).  
- Stay engaged until professional help is secured.
"""

def generate_response(user_number, message):
    """Generate AI response considering past conversations."""
    model = genai.GenerativeModel("gemini-2.5-pro-exp-03-25")

    # Retrieve the user's last 5 messages for context
    past_conversations = get_past_conversations(user_number, limit=5)
    past_context = "\n".join([f"User: {msg} | AI: {resp}" for msg, resp in past_conversations])

    prompt = f"""
    {SYSTEM_INSTRUCTIONS}
    Consider the previous conversation:
    
    {past_context}
    
    User Message: {message}
    """
    
    response = model.generate_content(prompt)
    return response.text.strip()

def classify_risk(message):
    """Classify the risk level of a user's message."""
    return classify_risk_with_model(message)
TWILIO_SMS_NUMBER = 'Twilio-registered SMS number'  # Your Twilio-registered SMS number
MY_PHONE_NUMBER = 'your phone number to receive alerts'  # Your phone number to receive alerts

def send_alert_to_phone(risk_message):
    """Send a high-risk message alert to your phone via Twilio SMS."""
    alert_message = f"🚨 High Risk Alert: {risk_message}"
    client = Client(ACCOUNT_SID, auth_token)
    message = twilio_client.messages.create(
        from_=TWILIO_SMS_NUMBER,
        body=alert_message,
        to=MY_PHONE_NUMBER  # Send alert via SMS
    )


@app.route("/whatsapp", methods=["POST"])
def whatsapp_webhook():
    incoming_msg = request.values.get("Body", "").strip()
    sender_number = request.values.get("From", "").strip()

    if not incoming_msg:
        return str(MessagingResponse())  # Return empty response
    risk_level = classify_risk(incoming_msg)

    # If risk is high, send an alert to your phone
    if risk_level == "high":
        send_alert_to_phone("User showing signs of distress. Immediate action required!")
    # Generate a response based on past conversations and current message
    response_text = generate_response(sender_number, incoming_msg)
    
    # Save the conversation (user message and bot response)
    save_conversation(sender_number, incoming_msg, response_text)
    
    # Create the Twilio response
    twilio_response = MessagingResponse()
    twilio_response.message(response_text)

    return str(twilio_response)  # Twilio expects XML, not JSON

def send_whatsapp_message(to, message):
    twilio_client.messages.create(
        from_=TWILIO_WHATSAPP_NUMBER,
        body=message,
        to=to
    )

if _name_ == "_main_":
    app.run(host="0.0.0.0", port=5000)
