# BingB Chatbot

![GitHub repo size](https://img.shields.io/github/repo-size/gvenkatn/bingb-chatbot)
![GitHub contributors](https://img.shields.io/github/contributors/gvenkatn/bingb-chatbot)
![GitHub stars](https://img.shields.io/github/stars/gvenkatn/bingb-chatbot?style=social)

## 🚀 About BingB Chatbot

### 🎯 Inspiration
As a student at SUNY Binghamton’s School of Computing, I noticed that students often struggle to find quick and accurate information regarding courses, faculty, and academic resources. The existing system, such as email-based ticketing for graduate program queries, helps streamline communication, but students still need a more immediate, interactive, and AI-powered solution for general inquiries.

Inspired by the need to **reduce email overload for faculty and staff** while improving the student experience, I developed **BingB Chatbot**—an AI-powered assistant designed to handle frequently asked questions related to **course registration, faculty details, program requirements, graduation, and more**. The chatbot serves as a **first point of contact** for students, offering instant responses and minimizing the need for repetitive email exchanges.

### 📚 What I Learned
Throughout the development of **BingB**, I gained valuable insights into:
- **Chatbot Development**: Designing conversation flows and structuring intelligent responses.
- **Natural Language Processing (NLP)**: Handling varied student queries effectively.
- **React UI Development**: Learning frontend technologies to build an interactive chatbot interface.
- **Backend & Database Management**: Optimizing PostgreSQL for structured information retrieval.
- **Deployment & Scalability**: Deploying on **Render** to ensure a seamless experience.

### 🛠️ How I Built It
The **BingB Chatbot** was built using:
- **Backend**: Python (FastAPI) with PostgreSQL for structured data storage.
- **Frontend**: A React-based UI for easy interaction.
- **Chatbot Engine**: Initially integrated with **Dialogflow**, later enhanced with a custom NLP approach.
- **Authentication**: Secure access to an admin panel for managing chatbot knowledge.
- **Deployment**: Hosted on **Render** for stability and accessibility.

### 🚧 Challenges Faced
Building **BingB** came with several hurdles, including:
- **Dialogflow Limitations**: Initial failures in retrieving course and faculty data led to custom NLP improvements.
- **Knowledge Base Expansion**: Structuring comprehensive and up-to-date information.
- **Frontend Development**: Overcoming limited experience with React while building the chatbot UI.
- **Authentication & Security**: Balancing ease of access with secure admin controls.
- **Deployment Optimization**: Ensuring a smooth deployment process without unnecessary dependencies like Alembic.

By reducing the reliance on **email-based queries** and providing students with an **instant, intelligent, and user-friendly assistant**, **BingB** significantly enhances the accessibility of academic information at the School of Computing. 🚀

## 🎥 Demo

[![Watch the demo](https://img.youtube.com/vi/YOUR_VIDEO_ID/maxresdefault.jpg)]([https://www.youtube.com/watch?v=YOUR_VIDEO_ID](https://youtube.com/shorts/BKOmhhEU_5k?feature=share))

Click the image above to watch a 30-second demo of the chatbot in action.

## 📦 Features
- Provides course and faculty details
- Answers FAQs with rich text formatting
- Secure admin panel with authentication
- User login functionality
- Intuitive React-based UI
- Deployed on Render

## 🔧 Installation

Clone the repository and install dependencies:

```sh
git clone https://github.com/your-username/bingb-chatbot.git
cd bingb-chatbot
npm install  # For UI dependencies
pip install -r requirements.txt  # For backend dependencies
```

## 🚀 Usage

Start the backend server:
```sh
python main.py
```

Start the frontend:
```sh
npm start
```

## 🤝 Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📬 Contact

For questions or suggestions, reach out at [venkatnarayan.official@gmail.com](mailto:venkatnarayan.official@gmail.com).

Was developed as a [hackathon project](https://build-your-own-ai-chat-bot.devpost.com/)

