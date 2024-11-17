/* eslint-disable react/jsx-no-undef */
import Link from 'next/link';

export default function Home() {
  return (
    <main className="min-h-screen bg-gradient-to-b from-gray-50 to-gray-100">
      <div className="max-w-7xl mx-auto px-4 py-16 sm:px-6 lg:px-8">
        <div className="text-center">
          <h1 className="text-4xl font-bold tracking-tight text-gray-900 sm:text-5xl md:text-6xl">
            Welcome to{' '}
            <span className="text-blue-600">Volkswagen Group</span>
          </h1>
          <p className="mt-3 max-w-md mx-auto text-base text-gray-500 sm:text-lg md:mt-5 md:text-xl md:max-w-3xl">
            Access your vehicle information, maintenance status, and more through our comprehensive dashboard.
          </p>
          <div className="mt-10">
            <Link href="/dashboard">
              <button className="bg-blue-600 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">
                Go to Dashboard
              </button>
            </Link>
          </div>
        </div>

        <div className="mt-20 grid grid-cols-1 gap-8 sm:grid-cols-2 lg:grid-cols-3">
          {features.map((feature) => (
            <div key={feature.title} className="p-6 bg-white rounded-lg shadow-md">
              <div className="text-lg font-medium text-gray-900">
                {feature.title}
              </div>
              <div className="mt-2 text-base text-gray-500">
                {feature.description}
              </div>
            </div>
          ))}
        </div>
      </div>
    </main>
  );
}

const features = [
  {
    title: 'Vehicle Monitoring',
    description: 'Real-time monitoring of your vehicle\'s health, performance, and maintenance needs.',
  },
  {
    title: 'Smart Charging',
    description: 'Track charging status and find nearby charging stations for your electric vehicle.',
  },
  {
    title: 'Predictive Maintenance',
    description: 'Stay ahead with AI-powered maintenance predictions and service recommendations.',
  },
  {
    title: 'Security Updates',
    description: 'Keep your vehicle secure with the latest cybersecurity updates and monitoring.',
  },
  {
    title: 'Personalization',
    description: 'Customize your driving experience with personalized settings and preferences.',
  },
  {
    title: 'Support Access',
    description: '24/7 access to customer support and vehicle assistance services.',
  },
];
