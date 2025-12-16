import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Layout from './components/layout/Layout/Layout';
import Home from './pages/Home/Home';
import About from './pages/About/About';
import Donate from './pages/Donate/Donate';
import Programs from './pages/Programs/Programs';
import Stories from './pages/Stories/Stories';
import GetInvolved from './pages/GetInvolved/GetInvolved';
import Contact from './pages/Contact/Contact';
import NotFound from './pages/NotFound/NotFound';
import './styles/variables.css';
import './styles/reset.css';
import './styles/global.css';
import './App.css';

function App() {
  return (
    <Router>
      <Layout>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/about" element={<About />} />
          <Route path="/donate" element={<Donate />} />
          <Route path="/programs" element={<Programs />} />
          <Route path="/stories" element={<Stories />} />
          <Route path="/get-involved" element={<GetInvolved />} />
          <Route path="/contact" element={<Contact />} />
          <Route path="*" element={<NotFound />} />
        </Routes>
      </Layout>
    </Router>
  );
}

export default App;