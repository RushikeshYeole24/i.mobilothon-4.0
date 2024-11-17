import { LucideIcon } from 'lucide-react';

export type SectionKey = 'home' | 'maintenance' | 'experience' | 'security' | 'compliance' | 'charging' | 'ai';

export interface Section {
  title: string;
  icon: LucideIcon;
  content: React.ReactNode;
}

export interface Notification {
  id: string;
  message: string;
  read: boolean;
}