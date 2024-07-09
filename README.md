# Emotional AI Project

## Overview

The Emotional AI project aims to create a comprehensive platform for introspection and emotional analysis. The project is structured to serve multiple purposes, including acting as an API server, providing an admin UI for data management and analysis, and planning for future expansion to include a cross-platform mobile version for public users.

## Emotional AI Book and The 3 Constants of Human Connection

Authored by MOCavada, the soon-to-be-published book "Emotional AI" explores the intricacies of human connections through the lens of artificial intelligence and introspection. The book introduces a groundbreaking theory known as the "3 Constants of Human Connection," which outlines fundamental elements that govern human interactions and relationships. These constants are:

1. **Change**: This constant highlights the dynamic nature of relationships, emphasizing the importance of actions (Act), reactions (React), and attractions (Attract) in shaping human connections.

2. **Power or Energy**: This constant delves into the forms of power that influence relationships, including negative/destructive power, positive/creative power, and neutral/equilibrium. Understanding these forces helps in navigating the complexities of emotional interactions.

3. **Moments**: This constant focuses on the temporal aspects of relationships, stressing the significance of past reflections, future insights, and present awareness. By introspecting on these moments, individuals can gain deeper insights into their interactions and connections.

## Project Structure

### Current Components

1. **API Server and Admin UI:**
   - **API Server:** The current `emotional AI` app serves as the backend API server, providing endpoints for data management, user authentication, and other necessary backend services.
   - **Admin UI:** This application includes an admin UI for managing and analyzing data, built using the `@carbon/themes` library.

### Future Components

2. **Public Web App:**
   - A future project will be initiated for the public-facing web app, utilizing UI libraries like Tailwind CSS or `schadcdn/ui` to design the user interface.

3. **Mobile App:**
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

## Example Directory Structure

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


### Dev Cheat Sheet

- ( Merget to Main branch )
git checkout main                  
git pull origin main
git checkout dev-branch
git rebase main
git checkout main                   /* merge main branch - - 

git merge dev-branch && git push origin main

## Reset to main last version
git checkout -b [new-branch]
git add . && git commit -m "test" && git push -f origin [new-branch]
git fetch
git reset --hard origin/main
git push -f origin main

- (Useful CLI)
rm package-lock.json && rm -rf node_modules
rm -rf .next && rm -rf out 
npx next info
npx next -h 

