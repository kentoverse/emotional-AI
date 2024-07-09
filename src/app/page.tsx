import Home from '@/src/views/home/Home';
import { HomePageAttributes } from '@/src/types';

export default function Page() {
  const pageData: HomePageAttributes = {
    greeting: 'Hi Authentic Human,',
    title: 'Welcome to Emotional AI',
    subtitle: 'The Emotional AI project aims to create a comprehensive platform for introspection and emotional analysis. The project is structured to serve multiple purposes, including acting as an API server, providing an admin UI for data management and analysis, and planning for future expansion to include a cross-platform mobile version for public users. Using IBM InspectorRAGet as the base for building our AI data model offers significant advantages, including a proven framework, advanced metrics, scalability, integration capabilities, and strong community support. These benefits make it an ideal foundation for developing a sophisticated and effective AI solution.',
    subtitleLink: {
      content: 'Learn More',
      href: 'https://github.com/kentoverse/emotional-AI',
      openInNewTab: true,
    },
    cards: [
      {
        title: 'Visualize',
        text: 'Experience analytics capabilities.',
        href: '/visualize',
        actionText: 'Try it out',
        tag: null,
        icon: 'CHART_MULTITYPE', // Ensure this matches the specific string literal
        openInNewTab: false,
      },
      {
        title: 'Examples',
        text: 'See how analytics platform can help you identify issues with the model faster.',
        href: '/examples',
        actionText: 'Explore',
        tag: null,
        icon: 'MICROSCOPE', // Ensure this matches the specific string literal
        openInNewTab: false,
      },
      {
        title: 'Data collection cookbooks',
        text: 'A guide for collecting human & algorithmic evaluations.',
        href: '/cookbooks',
        actionText: 'Start cooking',
        tag: 'coming soon',
        icon: 'NOODLE_BOWL', // Ensure this matches the specific string literal
        openInNewTab: false,
        disabled: true,
      },
      {
        title: 'Documentation',
        text: 'Access developer resources',
        href: '/documentation',
        actionText: 'Read the docs',
        tag: 'coming soon',
        icon: 'BOOK', // Ensure this matches the specific string literal
        openInNewTab: false,
        disabled: true,
      },
    ],
  };

  return <Home page={pageData} />;
}