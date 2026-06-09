# AI Fusion English Class Portfolio: Seosang High School

This repository contains the source code for an EdTech-Integrated Adaptive Language Learning & Collaborative Reading Web Application tailored for **Seosang High School 1st-grade English classes**. Built on the Streamlit framework, this application integrates cognitive vocabulary matching, AI-assisted context reading, a high-stakes peer review matrix, customized digital worksheets, and an integrated real-time classroom orchestration timer into a single unified web interface (`/Class_apps`).

---

## 🏫 1. Teaching Context([AI Fusion English Class 앱 바로가기](https://miniproject-7xx9z2n9e35xhxyzygdyj7.streamlit.app/))

* **Learners Profile:** The target learners are 1st-grade students at **Seosang High School** (mixed-ability, approximately 20–25 students per class). Students exhibit varying levels of intrinsic motivation, with a distinct polarization between upper-tier fluent readers and lower-tier students struggling with foundational syntax and core vocabulary.
* **Classroom Environment:** The lesson takes place in a fully upgraded smart-classroom ecosystem. Every student is equipped with a personal smart device (tablet, Chromebook, or smartphone) connected to high-speed school Wi-Fi. The front wall features an interactive smart board for synchronized instructor-led anchor scaffolding.
* **Learners' Challenges:**
    * **Vocabulary Retention Deficit:** Students struggle to transfer vocabulary from short-term recognition to active textual decoding during continuous reading tasks.
    * **Syntactic Multi-Tasking Overload:** Analyzing complex, compound structures in high school English textbooks triggers high cognitive fatigue, causing lower-tier readers to disengage entirely.
    * **Monolingual Expression Anxiety:** Students display extreme hesitance when prompted to formulate arguments or summarize English text segments orally, fearing peer judgment and lacking structural sentence starters.

---

## 🎯 2. Lesson Purpose

* **What it Teaches:** This lesson focuses on the academic reading text **"The Architecture of Nature & Human Innovation"** (or a core curriculum unit tailored for High School 1st grade). It explicitly trains students in text-scanning, identifying contextual cohesive devices, extracting core thematic arguments, and conducting structural peer-to-peer tutoring.
* **Why it is Meaningful:** Moving away from passive, teacher-led grammatical parsing, this lesson leverages an **Interactive Jigsaw II & Reciprocal Teaching framework**. It transforms complex reading into an accountability-driven, social learning experience. Each student owns a distinct portion of the text, engineering an authentic "need to communicate" in an EFL (English as a Foreign Language) environment while providing digital safety nets for low-achieving students.

---

## 🚀 3. App Purpose (`/Class_apps(https://miniproject-djyhkowbsqtoov8yham3m9.streamlit.app/)

* **Why it was Built:** The web application was engineered to unify isolated open-source tools into a zero-friction, single-URL interface. This removes the administrative overhead of directing students to multiple third-party URLs, minimizing distraction and safeguarding instructional time.
* **Learning Needs Addressed:**
    * **Scaffolded Lexical Decoding:** The integrated Word Canvas & Matching module provides low-stakes gamified retrieval, anchoring key vocabulary before text immersion.
    * **Differentiated Pacing for Tiered Groups:** Fast-finishers access deep-dive comprehension diagnostics and contextual extension questions, allowing the instructor to dedicate physical roaming time to scaffold struggling readers.
    * **Cross-Platform PDF Binary Streaming:** Eliminates CORS blocks and external login pop-ups, enabling instant local downloads of customized jigsaw worksheets directly through the mobile browser interface.

---

## 📐 4. App Design

* **How it Works:** The app utilizes a modular **Streamlit multipage navigation framework (`st.navigation`)**. It organizes specific instructional phases into independent sidebar routes. This keeps the student interface clear, distraction-free, and mapped sequentially to the lesson plan.
* **Data & Content Utilized:**
    * **Text/CSV Database:** Hosts structured datasets (`vocab_high1.csv`) and tiered reading comprehension engines (`assessment_matrix.csv`) containing multi-layered multiple-choice, syntax sorting, and contextual inference items complete with instant automated feedback loops.
    * **Media & TTS Streaming:** Embedded YouTube API handles latency-free video stream injection for schema activation. The system uses a Python-backed text-to-speech engine to generate real-time standard acoustic models for auditory reinforcement.
    * **Libraries & Components:** Built with core data wrappers, custom CSS layout wrappers for optimized mobile rendering, session state tracking (`st.session_state`) for preserving individual gamification milestones, and custom JavaScript components for interactive visual cues.
* **Learner Interaction:** Students interact through text input forms, interactive multiple-choice radio selectors, dynamic toggle buttons for text parsing hints, binary worksheet download triggers, and audio execution inputs.

---

## 📋 5. 50-Minute Lesson Plan & Classroom Use

### 📊 Lesson Procedure at a Glance

| Phase | Time | Learning Activities & Tasks | 🕹️ App Implementation & Improvements |
| :--- | :--- | :--- | :--- |
| **Introduction** | 5 min. | • Attendance check<br>• Dynamic vocabulary warm-up | **01 🕹️ Vocab Matching Game**<br>• Low-stakes gamified retrieval practice via drag-and-drop or string inputs to maximize initial engagement. |
| **Development 1** | 7 min. | • Pre-reading schema activation<br>• Text-topic prediction and inference | **02 🎬 Embedded Media Stream & Concept Anchor**<br>• Delivers zero-buffering background media or interactive image prompts directly within the app UI to trigger initial interest. |
| **Development 2** | 15 min. | • **Jigsaw Phase 1 (Expert Groups):** Students focus on assigned text segments, analyzing syntax and extracting core details. | **03 📘 Digital Worksheet & Text Helper**<br>• Distributes platform-agnostic PDFs.<br>• Provides a 'Hint Box' with syntax breakdowns for low-achieving students. |
| **Development 3** | 10 min. | • **Jigsaw Phase 2 (Home Groups):** Reciprocal teaching where experts synthesize and teach their assigned segment to peers. | **04 ⏳ Orchestration Class Timer**<br>• Displayed on the main smart board via the app interface to keep pacing strict, transparent, and focused. |
| **Development 4** | 7 min. | • Individual accountability assessment<br>• Meta-cognitive feedback loop | **05 📖 Tiered Quiz & Analytics Engine**<br>• Students complete individual comprehension and grammar diagnostics with instant automated reasoning breakdowns. |
| **Conclusion** | 5 min. | • Wrap-up, group reflection, and preview of upcoming extension writing. | **Physical Smart Board & Teacher Synthesis**<br>• Consolidates student findings and recognizes standout collaborative groups. |

---

## ⚠️ 6. Limitations

1.  **Session Isolation (Lack of Live Dashboard):** Student performance logs and quiz diagnostic metrics are compiled purely within the client's local browser memory. The instructor cannot access a synchronized live dashboard to monitor group-wide error rates concurrently without moving physically around the room.
2.  **Fixed Progression Velocity:** The vocabulary retrieval engine operates on a static CSV structure, meaning it cannot automatically scale its pacing, word length, or structural hints based on real-time student error frequency.
3.  **Client-Side Hardware Constraints:** Native browser differences on older student smartphones can occasionally lead to rendering variations or audio latency during text-to-speech playback.

---

## 🔮 7. Future Development

1.  **Cloud Database Integration (LRS connection):** Connecting a lightweight cloud layer (e.g., Firestore or Google Sheets API) to continuously capture student metrics (`st.session_state` logs), generating an instantaneous teacher dashboard for real-time formative guidance.
2.  **Algorithmic Adaptive Scaffolding:** Implementing an Item Response Theory (IRT) model that dynamically presents simplified sentence frames or structural hints if a student fails a vocabulary or reading task twice consecutively.
3.  **AI Voice Analytics (Speech-to-Text):** Integrating an open-source speech recognition loop to analyze pronunciation accuracy and structural confidence during the oral peer-tutoring jigsaw phase.
