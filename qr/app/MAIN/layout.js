import { Inter } from "next/font/google";
import Header from "../components/header/header";
import Footer from "../components/footer/footer";
import "../globals.css";
const inter = Inter({ subsets: ["latin"] });
export default function RootLayout({ children }) {
  return (
    <html lang="en">
        <body className={inter.className}>
        <Header/>
         {children}
        <Footer/>
        </body>
    </html>
  );
}