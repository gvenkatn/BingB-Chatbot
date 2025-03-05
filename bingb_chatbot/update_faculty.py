import psycopg2

# PostgreSQL connection details (Update as needed)
DB_NAME = "bingb"
DB_USER = "postgres"
DB_HOST = "localhost"
DB_PORT = "5432"

# Faculty data to update
faculty_updates = [
    {"name": "Prof. Thomas W. Bartenstein", "email": "tbartens@binghamton.edu", "office_location": "EB Q06", "phone_number": None, "research_interests": "Programming languages, Stream programming, Educational software, Computer architecture, Operating systems, Microprocessor design"},
    {"name": "Prof. Ali J. Ben Ali", "email": "abenali@binghamton.edu", "office_location": "EB Q06", "phone_number": "607-777-4806", "research_interests": "Mobile systems, Edge computing, Robotics, Autonomous systems, Machine learning"},
    {"name": "Prof. Hafiz Munsub Ali", "email": "hali@binghamton.edu", "office_location": "EB Q12", "phone_number": None, "research_interests": "Combinatorial optimization, Network planning, Social network analysis, Healthcare informatics"},
    {"name": "Prof. Anurag S Andhare", "email": "aandhar2@binghamton.edu", "office_location": "EB N22", "phone_number": None, "research_interests": "Machine learning systems, Deep learning, Large language models, Internet of Things"},
    {"name": "Prof. Eric Atkinson", "email": "eatkinson2@binghamton.edu", "office_location": "EB N16", "phone_number": "607-777-4326", "research_interests": "Programming languages, Program analysis, Formal methods"},
    {"name": "Prof. Jeremy Blackburn", "email": "jblackbu@binghamton.edu", "office_location": "EB N10", "phone_number": None, "research_interests": "Measurements, Data science, Social media, Social network analysis"},
    {"name": "Prof. Jayson Boubin", "email": "jboubin@binghamton.edu", "office_location": "EB N32", "phone_number": "607-777-4835", "research_interests": "Systems, Autonomous systems, Unmanned aerial vehicles, Edge computing"},
    {"name": "Prof. Patrick H. Chen", "email": "patrickchen@binghamton.edu", "office_location": "EB P13", "phone_number": "607-777-4953", "research_interests": "Machine learning, Natural language processing"},
    {"name": "Prof. Kenneth Chiu", "email": "kchiu@cs.binghamton.edu", "office_location": "EB Q15", "phone_number": None, "research_interests": "High-performance computing, Big data, Bioinformatics"},
    {"name": "Prof. Weiying Dai", "email": "wdai@binghamton.edu", "office_location": "EB N18", "phone_number": "607-777-4859", "research_interests": "Brain mapping, Biomedical imaging, Neuroimaging, Blood flow imaging, Functional MRI"},
    {"name": "Prof. Zeyu Ding", "email": "dding1@binghamton.edu", "office_location": "EB N34", "phone_number": "607-777-4824", "research_interests": "Privacy, Algorithmic fairness, Machine learning, Security"},
    {"name": "Prof. Jason Foos", "email": "jfoos1@binghamton.edu", "office_location": "EB Q13", "phone_number": "607-777-4826", "research_interests": None},
    {"name": "Prof. Dave Garrison", "email": "david.garrison@binghamton.edu", "office_location": "EB Q19", "phone_number": None, "research_interests": "Subnormality conditions in solvable groups, Commutator expansion formulas, Microcontrollers, Image processing, Scheduling algorithms"},
    {"name": "Prof. Kanad Ghose", "email": "ghose@cs.binghamton.edu", "office_location": "EB P10", "phone_number": "607-777-4608", "research_interests": "Computer architecture, Parallel processing, Power-aware systems, High-performance computing"},
    {"name": "Prof. Kartik Gopalan", "email": "kartik@binghamton.edu", "office_location": "ES 1402", "phone_number": "607-777-6237", "research_interests": "Cloud computing, Virtualization, Cybersecurity, Operating systems, Distributed systems"},
]

# Connect to PostgreSQL and update records
try:
    conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, host=DB_HOST, port=DB_PORT)
    cur = conn.cursor()
    
    # Update faculty details
    for faculty in faculty_updates:
        cur.execute("""
            UPDATE faculty
            SET office_location = %s, phone_number = %s, research_interests = %s
            WHERE email = %s
        """, (faculty["office_location"], faculty["phone_number"], faculty["research_interests"], faculty["email"]))
    
    conn.commit()
    print("✅ Faculty database updated successfully!")

except Exception as e:
    print(f"❌ Error updating database: {e}")

finally:
    if conn:
        cur.close()
        conn.close()
