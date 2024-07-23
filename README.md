# Yunigma Medical Chatbot

Yunigma is an AI-powered medical chatbot. It leverages Google's Gemini AI models to provide medical information and answer health-related queries.

<img width="1458" alt="Screenshot 2024-07-23 at 9 42 51 PM" src="https://github.com/user-attachments/assets/d1a873a8-6e38-4c88-b31c-7f0bfde0ee9d">

## Features

- Medical query answering using Gemini Pro model
- Image analysis for medical-related images using Gemini Pro Vision
- Multi-language support (English, Hindi, Kannada, Tamil, Telugu)
- User-friendly Streamlit interface
- Chat history persistence
- Input validation for medical relevance

## Prerequisites

Before you begin, ensure you have met the following requirements:
- Python 3.7+
- Streamlit
- Google GenerativeAI API key
- PIL (Python Imaging Library)
- googletrans

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/YashasJKumar/Medical_Chatbot.git
   cd Medical_Chatbot
   ```

2. Install the required packages:
   ```sh
   pip install -r requirements.txt
   ```

3. Set up your Google API key:
   - Create a `secrets.toml` file in the `.streamlit` directory
   - Add your Google API key:
     ```toml
     GOOGLE_API_KEY = "your-api-key-here"
     ```

## Usage

To run the Yunigma Medical Chatbot:

1. Navigate to the project directory
2. Run the Streamlit app:
   ```sh
   streamlit run app.py
   ```
3. Open your web browser and go to the provided local URL (usually `http://localhost:8501`)

## How to Use

1. Type your medical query in the chat input
2. Optionally, upload an image for analysis
3. Select your preferred response language from the sidebar
4. View the chatbot's response in your chosen language

## Disclaimer

This chatbot is trained on medical textbooks and is fine-tuned to answer medical-related queries. It is not a substitute for professional medical advice, diagnosis, or treatment. Always consult with a qualified healthcare provider for medical concerns.

## Contributing

Contributions to the Yunigma Medical Chatbot are welcome. Please ensure that your code adheres to the project's coding standards and includes appropriate tests.


## Contact

If you have any questions or feedback, please contact me at [yashasjkumar6@gmail.com].
