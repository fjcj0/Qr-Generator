import { Inter } from "next/font/google";
import "./globals.css";
import Header from './components/header/header';
import Footer from './components/footer/footer';
const inter = Inter({ subsets: ["latin"] });
export const metadata = {
  title: "Qr",
  description: "Generated by create next app",
};
export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body className={inter.className}>
          {children}
      </body>
    </html>
  );
}