# Emotional AI Project

## Overview

The Emotional AI project aims to create a comprehensive platform for introspection and emotional analysis. The project is structured to serve multiple purposes, including acting as an API server, providing an admin UI for data management and analysis, and planning for future expansion to include a cross-platform mobile version for public users.

In-developement Pubic View - [www.kentoverse.com](https://www.kentoverse.com).

## Emotional AI Book and The 3 Constants of Human Connection

Authored by MOCavada, the soon-to-be-published book “Emotional AI” explores the intricacies of human connections through the lens of artificial intelligence and introspection. The book introduces a theory based on MOCavada’s personal experiences, known as the “3 Constants of Human Connection,” which outlines fundamental elements that govern human interactions and relationships.

The book premise aligns with the goal to create an introspective guide and incorporate Emotional AI to support users in understanding and improving their connections.

These 3 constants are:

1. **Change (Dynamics of Interaction)**: This constant highlights the dynamic nature of relationships, emphasizing the importance of actions (Act), reactions (React), and attractions (Attract) in shaping human connections.

2. **Power (Effects we Attract)**: This constant delves into the forms of power that influence relationships, including negative/destructive power, positive/creative power, and neutral/equilibrium. Understanding these forces helps in navigating the complexities of emotional interactions.

3. **Moments (Lifetime Influences that Connects)**: This constant focuses on the temporal aspects of relationships, stressing the significance of past reflections, future insights, and present awareness. By introspecting on these moments, individuals can gain deeper insights into their interactions and connections.

## Purpose

To create an app that guides users through introspection using “The 3 Constants of Human Connection.” This app will teach users how to understand their interactions, the influences of these interactions, and the underlying causes rooted in our past and present experiences can define potential outcomes in our future.

## The Introspection Process

1. **Interactions from our Need to Connect**: This step focuses on understanding the initial interactions that stem from our inherent need to connect with others.
2. **Effects that we Attract from our Interactions**: This step examines the effects that attract and influence future interactions based on our initial connections.
3. **Effects that are Influenced by our Past and Present**: This step delves into how past experiences and memories influence our current interactions and connections.

## Application of Emotional AI

The AI component of the app will assist users in:

- **Analyzing their interactions (Act, React, Attract)**
- **Understanding the influences of these interactions (Negative, Positive, Balanced)**
- **Reflecting on past experiences, forecasting future outcomes, and maintaining present awareness**

This updated premise aligns with your goal to create an introspective guide and incorporate Emotional AI to support users in understanding and improving their connections.

## Introspection Algorithms

OpenAI can be used to implement and enhance the introspection algorithm by referring to the 3 Constants of Human Connections. Here’s how it can be done:

### 1. Change – Dynamics of Interaction

**Algorithm Explanation**:

- **Act**: Identify and analyze initial interactions, such as changing the topic in a conversation.
- **React**: Understand and interpret responses to these actions, determining how they ignite subsequent interactions.
- **Attract**: Analyze what aspects of the interaction attract and maintain engagement.

**Implementation with OpenAI**:

- **Act**: Use the model to parse user inputs and detect initial actions.
- **React**: Generate possible reactions and interpret the sentiment and context of these reactions.
- **Attract**: Identify key elements that drive engagement or attraction within the interaction.

### 2. Power – Attracts Influence and Effects

**Algorithm Explanation**:

- **Negative Effects**: Detect and categorize interactions leading to negative outcomes.
- **Positive Effects**: Identify interactions resulting in positive engagement and reinforcement.
- **No Effect/Balance**: Recognize neutral interactions that maintain a state of equanimity.

**Implementation with OpenAI**:

- Analyze interactions to classify them into negative, positive, or neutral categories.
- Provide insights or feedback based on the classified interaction types to help users understand their impact.

### 3. Moments – Connections of Our Lifetime

**Algorithm Explanation**:

- **Past Reflections**: Encourage users to reflect on past experiences and how they influence current interactions.
- **Future Insights**: Provide predictions or insights into potential future outcomes based on current patterns.
- **Present Awareness**: Enhance present-moment awareness and mindfulness in interactions.

**Implementation with OpenAI**:

- Generate prompts and questions that guide users in reflecting on past experiences.
- Use predictive models to offer insights into possible future scenarios based on current behavior patterns.
- Enhance real-time feedback to promote present-moment awareness during interactions.

## Integrating OpenAI with Introspection Algorithm

1. **Input Parsing**: OpenAI can process and understand user inputs, identifying key elements of the interaction.
2. **Contextual Understanding**: The model can maintain context over a conversation, providing relevant and consistent feedback.
3. **Response Generation**: Based on the 3 Constants, OpenAI can generate responses that guide users through introspection, offering personalized insights and feedback.

## Example Workflow

1. **User Input**: The user describes an interaction or reflects on a past experience.
2. **Analysis**:
   - **Change**: The model analyzes the dynamics of the interaction (Act, React, Attract).
   - **Power**: It classifies the effects of the interaction (negative, positive, neutral).
   - **Moments**: It helps the user connect the interaction to past experiences, present awareness, and future possibilities.
3. **Output**: The model generates an introspective response, helping the user understand their actions and emotions better.

By leveraging OpenAI’s capabilities, you can create an effective and engaging introspection tool that aligns with the 3 Constants of Human Connections, providing users with meaningful insights and guidance.

## Project Structure

### Current Components

1. **API Server and Admin UI:**

### API Server 
- The current `emotional AI` app serves as the backend API server, providing endpoints for data management, user authentication, and other necessary backend services.
### Admin UI

- This application includes an admin UI for managing and analyzing data, built using the `@carbon/themes` library.
-  Build the admin interface using `@carbon/themes` within the same application.
- Implement features for data management and analysis accessible only to authorized admin users.

## Future Components


### 1. Public Web App
- Start a new project for the public-facing web app.
- Use Next.js app with server components to design the UI.
- Connect the web app to the backend API for data and user interactions.
   - A future project will be initiated for the public-facing web app, utilizing UI libraries like Tailwind CSS or `schadcdn/ui` to design the user interface.

### 2. Mobile App
   - A cross-platform mobile app will be developed using frameworks such as React Native or Flutter, ensuring optimized mobile experiences for public users.

## Why We Are Using IBM InspectorRAGet as Our Base for Building Our Own AI Data Model

**1. Proven Framework and Tools:** IBM InspectorRAGet is a robust platform designed specifically for the introspection and evaluation of Retrieval-Augmented Generation (RAG) models. Its advanced framework provides tools for performance benchmarking, combined aggregate and instance-level analysis, and offers a holistic view of results through various metrics. This ensures a solid foundation for developing and refining our AI models.

**2. Advanced Metrics and Evaluation:** InspectorRAGet enables detailed performance benchmarking and comprehensive evaluation techniques, which are crucial for identifying the strengths and weaknesses of our AI models. These capabilities help in targeting improvements more accurately and achieving better results.

**3. Customizable and Scalable:** The platform’s modular and scalable design allows for extensive customization to meet specific project requirements. This flexibility ensures that we can tailor the tool to fit the unique needs of our introspection and AI data model development.

**4. Integration Capabilities:** InspectorRAGet’s ability to integrate with other tools and platforms allows for seamless incorporation into our broader AI development ecosystem. This integration is essential for creating comprehensive AI solutions that leverage multiple data sources and tools efficiently.

**5. Community and Support:** As an IBM product, InspectorRAGet benefits from extensive community support and detailed documentation. This support is invaluable for troubleshooting, learning best practices, and staying updated with the latest advancements in AI and machine learning.

### Official Description of IBM InspectorRAGet

> "An introspection Platform for RAG Evaluation enabling performance benchmarking, a combined aggregate and instance-level analysis, a holistic view of results via a mix of metrics, annotator qualification, and dataset characterization. Our goal is to help accelerate the transition from idea to product."

### Additional Benefits

- **Data Management:** Robust data management features ensure efficient and secure handling of data.
- **Performance Benchmarking:** Enables detailed performance benchmarking, critical for developing high-quality AI models.
- **Holistic Analysis:** Provides a holistic analysis of AI models, leading to more comprehensive and reliable results.

### Conclusion

Using IBM InspectorRAGet as the base for building our AI data model offers significant advantages, including a proven framework, advanced metrics, scalability, integration capabilities, and strong community support. These benefits make it an ideal foundation for developing a sophisticated and effective AI solution.

For more information, refer to the [IBM InspectorRAGet documentation](https://www.ibm.com/docs/en).

## Benefits

- **Separation of Concerns:** Keeping the admin UI and the public-facing UI separate allows for tailored interfaces for each audience without unnecessary complexity.
- **Scalability:** The backend API can serve multiple clients (admin UI, public web app, mobile app), making the architecture scalable.
- **Flexibility:** Different UI libraries can be used for different parts of the project, providing flexibility in tool choice.
- **Maintainability:** Separation of the admin and public interfaces makes the codebase easier to maintain and update.

## Implementation Steps

### API Server

- Ensure the backend (currently part of the `emotional AI` app) is designed as a RESTful API or GraphQL API.
- Secure the API with authentication and authorization mechanisms.

### Admin UI

- Build the admin interface using `@carbon/themes` within the same application.
- Implement features for data management and analysis accessible only to authorized admin users.

### Public Web App

- Start a new project for the public-facing web app.
- Use Tailwind CSS or `schadcdn/ui` to design the UI.
- Connect the web app to the backend API for data and user interactions.

### Mobile App

- Plan for a future cross-platform mobile app using frameworks like React Native or Flutter.
- Ensure the mobile app interacts with the same backend API for a consistent user experience across platforms.






## Directory Structure

```plaintext
emotional-AI/
├── backend/
│   ├── app.py
│   ├── requirements.txt
│   ├── Dockerfile
│   └── ...
├── admin-ui/
│   ├── src/
│   ├── public/
│   ├── package.json
│   ├── Dockerfile
│   └── ...
├── public-web-app/
│   ├── src/
│   ├── public/
│   ├── package.json
│   └── ...
├── mobile-app/
│   ├── src/
│   ├── android/
│   ├── ios/
│   ├── package.json
│   └── ...
└── docker-compose.yml

