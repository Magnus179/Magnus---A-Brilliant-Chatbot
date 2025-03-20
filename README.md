# Chatbot System Overview
A Django-powered chatbot designed to deliver intelligent responses based on stored questions. It includes a robust backend using Django ORM, ensuring accurate query handling. The chatbot dynamically fetches real-time date and time information and logs unanswered queries for future improvement.

# UI View
<h3><b> Chatbot Dashboard </b></h3>
<ul>
  <li>A structured interface displaying recent conversations and suggested questions.</li>
  <li>Search functionality to find past interactions.</li>
  <li>Prominent "Ask a Question" input field for seamless user interaction.</li>
</ul>



<h3><b>Chat Interface</b></h3>
<ul>
  <li> A real-time chatbox where users can ask questions. </li>
   <li>Instant responses fetched from a pre-populated FAQ database.</li>
   <li>Intelligent keyword matching ensures responses even if partial phrases match. </li>
   <li>Instant responses fetched from a pre-populated FAQ database.</li>
  <li>Displays timestamps for questions and responses.</li>
</ul>

 <h3><b>Unanswered Questions Log</b></h3>
Stores user queries that don't match existing FAQs.
Admin panel for reviewing and adding answers to improve chatbot performance.
 
Answer Detail View <h3><b>Chat Interface</b></h3>
Displays full question and response history.
Provides metadata such as query time, response time, and accuracy level.

<h3><b>Edit & Improve Responses  </b></h3>
Admin can modify or enhance chatbot responses via a structured form.
Logs edits and updates for better tracking.

<h3><b>Delete Confirmation Model </b></h3>
A modal popup appears before deleting a stored question or answer.
Options to confirm or cancel deletion for data integrity.

# Design & Accessibility
<ul>
  <li>Modern UI with a responsive and intuitive layout.</li>
   <li>Styled using Bootstrap/CSS for a professional look.</li>
   <li>
Fully accessible, adhering to WCAG guidelines.</li>
   <li>Optimized for both desktop and mobile experiences.</li>
</ul>


