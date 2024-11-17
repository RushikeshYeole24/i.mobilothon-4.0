"use client"; 
/* eslint-disable @typescript-eslint/no-unused-vars */
import React, { useState } from 'react';
import {
  Car,
  Users,
  Shield,
  FileText,
  Battery,
  Brain,
  ChevronRight,
  Settings,
  Bell,
  LucideIcon
} from 'lucide-react';
import VWID4SVG from './components/vw-svg';

// Define types for our sections
type SectionKey = 'home' | 'maintenance' | 'experience' | 'security' | 'compliance' | 'charging' | 'ai';

interface Section {
  title: string;
  icon: LucideIcon;
  content: React.ReactNode;
}

const Dashboard = () => {
  const [activeSection, setActiveSection] = useState<SectionKey>('home');
  const [notifications, setNotifications] = useState([
    'Engine oil change recommended in 2000 km',
    'Software update available for infotainment system',
    'Tire pressure optimal'
  ]);

  const sections: Record<SectionKey, Section> = {
    home: {
      title: 'Welcome to Volkswagen Group',
      icon: Car,
      content: (
        <div className="space-y-6">
          <div className="h-[400px] w-full bg-gradient-to-b from-gray-50 to-gray-100 rounded-lg overflow-hidden p-4">
            <VWID4SVG />
          </div>
          <div className="grid grid-cols-3 gap-4">
            <div className="p-4 bg-white shadow-md rounded-lg">
              <h4 className="font-semibold">Vehicle Status</h4>
              <p className="text-green-600">All Systems Normal</p>
            </div>
            <div className="p-4 bg-white shadow-md rounded-lg">
              <h4 className="font-semibold">Next Service</h4>
              <p>In 3,000 km</p>
            </div>
            <div className="p-4 bg-white shadow-md rounded-lg">
              <h4 className="font-semibold">Battery Level</h4>
              <p>95%</p>
            </div>
          </div>
        </div>
      )
    },
    maintenance: {
      title: 'Predictive Maintenance',
      icon: Car,
      content: (
        <div className="space-y-4">
          <div className="grid grid-cols-2 gap-4">
            <div className="p-4 bg-gray-50 shadow-md rounded-lg">
              <h4 className="font-semibold mb-2">Engine Health</h4>
              <div className="text-2xl font-bold text-green-600">98%</div>
            </div>
            <div className="p-4 bg-gray-50 shadow-md rounded-lg">
              <h4 className="font-semibold mb-2">Battery Status</h4>
              <div className="text-2xl font-bold text-green-600">95%</div>
            </div>
          </div>
          <div className="p-4 bg-yellow-100 border-l-4 border-yellow-500 rounded-lg">
            <p>Next maintenance scheduled in 3,000 km</p>
          </div>
        </div>
      )
    },
    experience: {
      title: 'Customer Experience',
      icon: Users,
      content: (
        <div className="space-y-4">
          <div className="p-4 bg-white shadow-md rounded-lg">
            <h4 className="font-semibold mb-2">Personalization Settings</h4>
            <div className="space-y-2">
              <div className="flex items-center justify-between">
                <span>Seat Position Memory</span>
                <Settings className="w-5 h-5" />
              </div>
              <div className="flex items-center justify-between">
                <span>Climate Preferences</span>
                <Settings className="w-5 h-5" />
              </div>
            </div>
          </div>
        </div>
      )
    },
    security: {
      title: 'Cybersecurity',
      icon: Shield,
      content: (
        <div className="space-y-4">
          <div className="p-4 bg-red-100 border-l-4 border-red-500 rounded-lg">
            <p>System security status: Protected</p>
          </div>
          <div className="p-4 bg-white shadow-md rounded-lg">
            <h4 className="font-semibold mb-2">Last Security Scan</h4>
            <p>Today, 14:30</p>
          </div>
        </div>
      )
    },
    compliance: {
      title: 'Regulatory Compliance',
      icon: FileText,
      content: (
        <div className="space-y-4">
          <div className="p-4 bg-white shadow-md rounded-lg">
            <h4 className="font-semibold mb-2">Emissions Status</h4>
            <div className="text-green-600">Compliant</div>
          </div>
        </div>
      )
    },
    charging: {
      title: 'Charging Infrastructure',
      icon: Battery,
      content: (
        <div className="space-y-4">
          <div className="grid grid-cols-2 gap-4">
            <div className="p-4 bg-white shadow-md rounded-lg">
              <h4 className="font-semibold mb-2">Nearest Station</h4>
              <p>2.5 km away</p>
            </div>
            <div className="p-4 bg-white shadow-md rounded-lg">
              <h4 className="font-semibold mb-2">Range</h4>
              <p>350 km</p>
            </div>
          </div>
        </div>
      )
    },
    ai: {
      title: 'AI Service Support',
      icon: Brain,
      content: (
        <div className="space-y-4">
          <div className="p-4 bg-white shadow-md rounded-lg">
            <h4 className="font-semibold mb-2">Virtual Assistant</h4>
            <button className="bg-blue-600 text-white px-4 py-2 rounded-lg">
              Start Chat
            </button>
          </div>
        </div>
      )
    }
  };

  return (
    <div className="min-h-screen bg-gray-100 p-8">
      <div className="max-w-7xl mx-auto">
        <div className="flex justify-between items-center mb-8">
          <h1 className="text-3xl font-bold">Volkswagen Group Dashboard</h1>
          <div className="flex items-center space-x-4">
            <button className="relative">
              <Bell className="w-6 h-6" />
              <span className="absolute -top-1 -right-1 bg-red-500 text-white text-xs rounded-full w-4 h-4 flex items-center justify-center">
                {notifications.length}
              </span>
            </button>
          </div>
        </div>

        <div className="grid grid-cols-12 gap-8">
          <div className="col-span-3 space-y-2">
            {(Object.keys(sections) as SectionKey[]).map((key) => (
              <button
                key={key}
                onClick={() => setActiveSection(key)}
                className={`w-full flex items-center justify-between p-4 rounded-lg ${
                  activeSection === key
                    ? 'bg-blue-600 text-white'
                    : 'bg-white hover:bg-gray-50'
                }`}
              >
                <div className="flex items-center space-x-3">
                  {React.createElement(sections[key].icon, { className: "w-5 h-5" })}
                  <span>{sections[key].title}</span>
                </div>
                <ChevronRight className="w-5 h-5" />
              </button>
            ))}
          </div>

          <div className="col-span-9">
            <div className="p-6 bg-white shadow-md rounded-lg">
              <h2 className="text-2xl font-bold mb-6">
                {sections[activeSection].title}
              </h2>
              {sections[activeSection].content}
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Dashboard;
