**INTRODUCTION:**

Dark Patterns Buster Hackathon is a pioneering initiative aimed at equipping students with a platform to combat deceptive design practices in the digital world. Our mission is to foster a culture of ethical innovation and problem-solving, addressing the pressing issues we encounter in our online experiences.


DarkDetect is a Chrome extension designed to identify and highlight dark patterns present on e-commerce websites. It scans and analyzes the text content on product pages, categorizing and classifying potential dark patterns. Once identified, these deceptive elements are highlighted, accompanied by a popup that provides information about the specific dark pattern category.

The successful implementation of this project owes much to the research presented in the paper titled "Dark Patterns at Scale: Findings from a Crawl of 11K Shopping Websites" by Mathur et al. We express our gratitude for the valuable dataset of dark pattern strings provided by the researchers, which played a crucial role in training our classification model. Additionally, their innovative page segmentation algorithm, which dissects webpages into meaningful text blocks, significantly contributed to the effectiveness of our dark pattern detection. Most importantly, their extensive work heightened our awareness of these unethical design practices in the online shopping landscape.
**TEAM NAME :** GOAL DIGGERS

**OUR TEAM:**

          1. KUWAR JAIN

          2. POORNIMA THAKUR
          
          3. AGAMJOT SINGH
          
          4. CHETAN
          
          5. TUSHAR SAHNI

Dark patterns are design tricks used to influence the way users interact with software. While some dark patterns are harmless, like emphasizing signup buttons with color, others can be more malicious in problematic. In the context of online stores, dark patterns can be used to nudge buyers into buying items they might not need.

**PROPOSED SOLUTION:**

Utilizing A Chrome Extension For Capturing Instances Of Dark Patterns On Websites.

**TECH STACK:**

The Chrome Extension front-end that scrapes the active web page is written in Javascript. For the back-end, a Python server running Flask interfaces Bernoulli Naive Bayes models to classify tokens of text sent to it.

Our solution utilizes a multifaceted approach, combining web scraping and Natural Language Processing (NLP) techniques to analyze text content and identify deceptive design tactics. One notable feature of our extension is the dynamic redirection mechanism, which guides users to an educational resource on Optical Character Recognition (OCR) technology when traditional scraping methods encounter obstacles.
While our solution does not directly integrate OCR functionality, the dynamic redirection serves as a proactive measure to educate users about potential alternatives in data extraction.

**RESULT:**

The website strategically highlights dark patterns with a distinctive red color, effectively bringing them to the user's attention and elucidating their nature and specific types. 
Furthermore, users gain access to a detailed pie chart showcasing the percentage breakdown of different dark pattern categories. This not only serves to enhance user awareness but also provides a comprehensive visual representation, enabling users to grasp the prevalence and diversity of deceptive tactics employed on the website.

**CONCLUSION:**

In summary, our project successfully tackles the crucial issue of identifying and countering deceptive user interface tactics on e-commerce platforms. Through the integration of web scraping, Natural Language Processing (NLP), and machine learning, we've created a robust Chrome extension capable of identifying and highlighting dark patterns. This empowers users to make more informed decisions during their online shopping experience.
Looking forward, we envision further enhancements to our project, including the incorporation of advertisement analysis capabilities and scalability improvements. By continuously refining and expanding our solution, our goal is to create a lasting impact by fostering trust, transparency, and fairness in online transactions.

**Installation:**

To begin installation, first clone this repository, or download and unzip it.

Install and run the Flask app backend by navigating to api, installing required libraries, and running app.py with Python

Install the Chrome extension:

Navigate to chrome://extensions
Enable "Developer mode" by toggling the switch at the top right of the page
Click the "Load unpacked" button.
Navigate to the repository directory, and select the folder app for installation
Ensure that the extension is enabled, and if so, the extension has been successfully installed!
