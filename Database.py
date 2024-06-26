from sqlalchemy import create_engine, Column, Integer, String, Boolean, Text, ForeignKey, Table, insert
from sqlalchemy.orm import sessionmaker, declarative_base, relationship
from sqlalchemy.exc import IntegrityError
import random

engine = create_engine('sqlite:///my_database.db')
Session = sessionmaker(bind=engine)
Base = declarative_base()

association_table = Table('prerequisite_association', Base.metadata,
    Column('course_id', String, ForeignKey('Course.class_id'), primary_key=True),
    Column('prerequisite_id', String, ForeignKey('Course.class_id'), primary_key=True)
)


class Course(Base):
    __tablename__ = 'Course'
    class_id = Column(String, primary_key = True) 
    cname = Column(String, nullable = False)
    fall = Column(Boolean)
    spring = Column(Boolean)
    summer = Column(Boolean)
    comp_sci = Column(Boolean)
    data_sci = Column(Boolean)
    info_sci = Column(Boolean)
    info_tech = Column(Boolean)
    info_sys = Column(Boolean)
    communication = Column(Boolean)
    humanities = Column(Boolean)
    social_sci = Column(Boolean)
    math_stats = Column(Boolean)
    science = Column(Boolean)
    completed = Column(Boolean, nullable = False)
    credit_hrs = Column(Integer, nullable = False)
    description = Column(Text)
    prerequisites = relationship('Course', secondary=association_table,
                                 primaryjoin=class_id == association_table.c.course_id,
                                 secondaryjoin=class_id == association_table.c.prerequisite_id,
                                 backref='prerequisite_of')

    def __repr__(self):
        return f"Course: {self.class_id} Course Name: {self.cname}"
    


Base.metadata.create_all(engine)
session = Session()

course_details = [
    #School of Computing Courses
    {'class_id': 'COP 2220', 'cname': 'Programming I', 'fall': True, 'spring': True, 'summer': True,'comp_sci' : True, 'data_sci' : True, 'info_sci' : True, 'info_tech' : True, 'info_sys' : True, 'communication': False, 'humanities' : False, 'social_sci': False, 'math_stats' : False, 'science' : False, 'completed': False, 'credit_hrs': 3, 'description': 'This course provides an introduction to problem solving techniques and the computer programming process. Topics in the course include data types, operations, expressions, flow control, I/O, functions, program structure, software design techniques, and memory allocation. Course concepts are reinforced with many programming projects throughout the course.'},
    
    {'class_id': 'COT 3100', 'cname': 'Computational Structures', 'fall': 1, 'spring': 1, 'summer': 1, 'comp_sci' : True, 'data_sci' : True, 'info_sci' : True, 'info_tech' : True, 'info_sys' : True, 'communication': False, 'humanities' : False, 'social_sci': False, 'math_stats' : False, 'science' : False, 'completed': False, 'credit_hrs': 3, 'description': 'This course will cover the mathematical and logical fundamentals required in computer science, information systems, information science, and information technology. The course develops concepts in discrete mathematical structures as applied to computing in general through the topics of sets; logic; proof techniques; Boolean algebra; algorithms and problem solving; number systems; number theory; counting and discrete probability; and relations and graphs.'},
    
    {'class_id': 'CIS 3253', 'cname': 'Legal and Ethical Issues in Computing', 'fall': 1, 'spring': 1, 'summer': 1, 'comp_sci' : True, 'data_sci' : True, 'info_sci' : True, 'info_tech' : True, 'info_sys' : True, 'communication': True, 'humanities' : False, 'social_sci': False, 'math_stats' : False, 'science' : False, 'completed': False, 'credit_hrs': 3, 'description': 'This course provides an opportunity to discuss and analyze the legal and ethical issues facing today’s computing professionals, as well as the legal and ethical issues computing professionals may face in the future. Legal and ethical issues are considered from local, as well as global perspectives.'},
    
    {'class_id': 'COP 3503', 'cname': 'Programming II', 'fall': 1, 'spring': 1, 'summer': 1, 'comp_sci' : True, 'data_sci' : True, 'info_sci' : True, 'info_tech' : True, 'info_sys' : True, 'communication': False, 'humanities' : False, 'social_sci': False, 'math_stats' : False, 'science' : False, 'completed': False, 'credit_hrs': 3, 'description': 'This course serves as a continuation to the Programming I course. Students are shown additional fundamental concepts of problem solving using the object-oriented paradigm and data structures. The topics in this course include classes, interfaces, objects, class types, events, exceptions, control structures, polymorphism, inheritance, linked lists, arrays, stacks, queues, and deques. Students are expected to apply these concepts through the construction of numerous small software systems using both integrated development environments and command-line- driven tools that support editing, testing, and debugging.'},
    
    {'class_id': 'CDA 3100', 'cname': 'Computer Organization and Architecture', 'fall': 0, 'spring': 1, 'summer': 0, 'comp_sci' : True, 'data_sci' : False, 'info_sci' : False, 'info_tech' : False, 'info_sys' : False, 'completed': False, 'communication': False, 'humanities' : False, 'social_sci': False, 'math_stats' : False, 'science' : False, 'credit_hrs': 4, 'description': 'This course will cover the fundamental ideas in computer architecture and organization. Topics include machine-level data representation; digital logic; computer arithmetic; processor design; system components and inter-communication; memory hierarchy; multi-core processors; GPU; and modern technological advancements.'},
    
    {'class_id': 'COT 3210', 'cname': 'Theory of Computation', 'fall': 1, 'spring': 0, 'summer': 0, 'comp_sci' : True, 'data_sci' : False, 'info_sci' : False, 'info_tech' : False, 'info_sys' : False, 'completed': False, 'communication': False, 'humanities' : False, 'social_sci': False, 'math_stats' : False, 'science' : False, 'credit_hrs': 3, 'description': 'This course will cover the theory of computation using formal methods for describing and analyzing programming languages and algorithms. Topics include finite automata and regular expressions; formal languages and syntactic analysis; pushdown automata and Turing machines; and computational complexity.'},
    
    {'class_id': 'COP 3530', 'cname': 'Data Structures', 'fall': 1, 'spring': 1, 'summer': 1, 'comp_sci' : True, 'data_sci' : True, 'info_sci' : True, 'info_tech' : True, 'info_sys' : True, 'communication': False, 'humanities' : False, 'social_sci': False, 'math_stats' : False, 'science' : False, 'completed': False, 'credit_hrs': 3, 'description': 'Students in this course will study various data structures including binary trees, balanced trees, B-trees, hashing, and heaps. Additional topics include advanced data structures such as splay trees, tree representations, graphs, dynamic memory, and algorithms for sorting and searching. Students are expected to complete projects using object-oriented programming.'},
    
    {'class_id': 'CNT 4504', 'cname': 'Computer Networks', 'fall': 1, 'spring': 1, 'summer': 1, 'comp_sci' : True, 'data_sci' : True, 'info_sci' : True, 'info_tech' : True, 'info_sys' : True, 'communication': False, 'humanities' : False, 'social_sci': False, 'math_stats' : False, 'science' : False, 'completed': False, 'credit_hrs': 3, 'description': 'In this course, students will study architectures, protocols, and layers in computer networks and develop client-server applications. Topics include the OSI and TCP/IP models, transmission fundamentals, flow and error control, switching and routing, network and transport layer protocols, local and wide-area networks, wireless networks, client-server models, and network security. Students will extend course topics via programming assignments, library assignments and other requirements.'},
    
    {'class_id': 'COP 3703', 'cname': 'Introduction to Databases', 'fall': 1, 'spring': 1, 'summer': 1, 'comp_sci' : True, 'data_sci' : True, 'info_sci' : True, 'info_tech' : True, 'info_sys' : True, 'communication': False, 'humanities' : False, 'social_sci': False, 'math_stats' : False, 'science' : False, 'completed': False, 'credit_hrs': 3, 'description': 'This course covers database modeling with emphasis on the relational data model. Principles of relational database design, normal forms, constraints, and SQL programming will be discussed extensively. Additionally, topics related to indexing, views, transactions, XML and No-SQL databases will also be discussed. The course will cover aspects of information security and assurance as they relate to data management. Concepts covered in the course will be reinforced through the use of open source and/or commercial database management systems.'},
    
    {'class_id': 'COP 3404', 'cname': 'Systems Programming', 'fall': 1, 'spring': 0, 'summer': 0, 'comp_sci' : True, 'data_sci' : False, 'info_sci' : False, 'info_tech' : False, 'info_sys' : False, 'communication': False, 'humanities' : False, 'social_sci': False, 'math_stats' : False, 'science' : False, 'completed': False, 'credit_hrs': 3, 'description': 'Students will learn the design and role of systems software including assemblers, loaders and linkers; assembly programming; system libraries; utility programs; concurrent programming including threads, semaphores, and synchronization; event-driven programming; memory management; and machine-dependent code optimization techniques.'},
    
    {'class_id': 'COP 4620', 'cname': 'Construction of Language Translators', 'fall': 0, 'spring': 1, 'summer': 0, 'comp_sci' : True, 'data_sci' : False, 'info_sci' : False, 'info_tech' : False, 'info_sys' : False, 'communication': False, 'humanities' : False, 'social_sci': False, 'math_stats' : False, 'science' : False, 'completed': False, 'credit_hrs': 3, 'description': 'This course introduces students to the theoretical foundations and practical issues of designing language translators. Students will learn how to use compiler construction tools such as generators of scanners and parsers. Grammars, parsing, lexical analysis, syntax analysis, code generation, and optimization will also be discussed.'},
    
    {'class_id': 'CEN 4010', 'cname': 'Software Engineering', 'fall': 0, 'spring': 1, 'summer': 0, 'comp_sci' : True, 'data_sci' : False, 'info_sci' : True, 'info_tech' : False, 'info_sys' : False, 'communication': False, 'humanities' : False, 'social_sci': False, 'math_stats' : False, 'science' : False, 'completed': False, 'credit_hrs': 3, 'description': 'This course introduces students to fundamental Software Engineering concepts and current practices. Topics covered include: software process models; agile software development; requirements engineering; domain modeling; model-driven development; software architectures; design paradigms and patterns; project management, tracking, and release planning; collaborative development, testing, deployment, maintenance and evolution.'},
    
    {'class_id': 'COT 4400', 'cname': 'Design and Analysis of Algorithms', 'fall': 1, 'spring': 0, 'summer': 0, 'comp_sci' : True, 'data_sci' : True, 'info_sci' : False, 'info_tech' : False, 'info_sys' : False, 'communication': False, 'humanities' : False, 'social_sci': False, 'math_stats' : False, 'science' : False, 'completed': False, 'credit_hrs': 3, 'description': 'This course will introduce fundamental techniques for designing and analyzing algorithms, including asymptotic analysis; divide-and-conquer algorithms and recurrences; greedy algorithms; dynamic programming; and graph algorithms.'},
    
    {'class_id': 'CAP 4630', 'cname': 'Introduction to Artificial Intelligence', 'fall': 0, 'spring': 1, 'summer': 0, 'comp_sci' : True, 'data_sci' : False, 'info_sci' : False, 'info_tech' : False, 'info_sys' : False, 'communication': False, 'humanities' : False, 'social_sci': False, 'math_stats' : False, 'science' : False, 'completed': False, 'credit_hrs': 3, 'description': 'Course topics include heuristic techniques for problem-solving and decision making, control and search strategies, knowledge representation, logic, AI languages, and tools. Applications such as machine learning, natural language understanding, planning, and robotics will be included.'},
    
    {'class_id': 'COP 4610', 'cname': 'Operating Systems', 'fall': 0, 'spring': 1, 'summer': 0, 'comp_sci' : True, 'data_sci' : False, 'info_sci' : False, 'info_tech' : False, 'info_sys' : False, 'communication': False, 'humanities' : False, 'social_sci': False, 'math_stats' : False, 'science' : False, 'completed': False, 'credit_hrs': 3, 'description': 'Topics in this course include process management, memory management, file management, and I/O device management.'},
    
    {'class_id': 'COP 3855', 'cname': 'Web Systems Development', 'fall': False, 'spring': True, 'summer': False,'comp_sci' : False, 'data_sci' : False, 'info_sci' : True, 'info_tech' : False, 'info_sys' : True, 'communication': False, 'humanities' : False, 'social_sci': False, 'math_stats' : False, 'science' : False, 'completed': False, 'credit_hrs': 4, 'description': 'Students learn about the influence of local and global transaction processing, Internet, Web design and development, and Electronic Data Interchange on information systems. This course discusses the concepts and skills required to design and implement Web application systems using Model-view-controller (MVC) architecture. Students learn about how Web applications are developed using client-side and server-side scripting to implement internal and external business processes. After an introduction to the basic concepts of relational database systems and Object Relational Mapping (ORM) students will practice for storing and accessing data in the database.'},
    
    {'class_id': 'COP 4813', 'cname': 'Internet Programming', 'fall': True, 'spring': False, 'summer': False,'comp_sci' : False, 'data_sci' : False, 'info_sci' : True, 'info_tech' : False, 'info_sys' : True, 'communication': False, 'humanities' : False, 'social_sci': False, 'math_stats' : False, 'science' : False, 'completed': False, 'credit_hrs': 3, 'description': ' In this course students will use current technologies to develop Internet and web-based applications. The topics to be covered include client and server-side components for the WWW to facilitate client-server communication, web services, and an introduction to source control tools. Students will extend course topics via programming assignments, library assignments and other assigned activities.'},
     
    {'class_id': 'CDA 4010', 'cname': 'User Interface Design', 'fall': True, 'spring': False, 'summer': False,'comp_sci' : False, 'data_sci' : False, 'info_sci' : True, 'info_tech' : False, 'info_sys' : True, 'communication': False, 'humanities' : False, 'social_sci': False, 'math_stats' : False, 'science' : False, 'completed': False, 'credit_hrs': 3, 'description': 'This course introduces the fundamentals of effective interaction between humans and computers with an emphasis on software and physical elements. Good and bad interface designs are examined to reinforce proven interface design techniques. The phases and tools involved in the interaction design process are discussed, as well as how the interaction design process aligns with the Software Development Life Cycle (SDLC).'},
    
    {'class_id': 'CIS 4327', 'cname': 'Information Systems Senior Project I', 'fall': True, 'spring': False, 'summer': False,'comp_sci' : False, 'data_sci' : False, 'info_sci' : True, 'info_tech' : False, 'info_sys' : True, 'communication': False, 'humanities' : False, 'social_sci': False, 'math_stats' : False, 'science' : False, 'completed': False, 'credit_hrs': 3, 'description': 'First of a two-course senior project on systems development with a significant laboratory component. Students will learn system development life cycle methodologies and its phases including requirements specification, analysis, and design. Students will design and develop a prototype information system in the context of the project team environment.'},

    {'class_id': 'CAP 3784', 'cname': 'Introduction to Data Analytics', 'fall': False, 'spring': True, 'summer': False,'comp_sci' : False, 'data_sci' : True, 'info_sci' : True, 'info_tech' : False, 'info_sys' : True, 'communication': False, 'humanities' : False, 'social_sci': False, 'math_stats' : False, 'science' : False, 'completed': False, 'credit_hrs': 3, 'description': 'This course gives a broad overview of the various aspects of data analytics and visualizations. Students will learn ways of accessing data from various sources such as web APIs and repositories, techniques of cleaning data and organizing data for analysis, using analytical methods to solve real-world problems, and create visualizations to aid the interpretation of analysis results. Students will have hands on training using relevant programming languages, as well as analytics and visualization tools. Over the course of the semester, students will apply lessons learned and use tools trained to work on exploratory and descriptive data science projects.'},

    {'class_id': 'CIS 4328', 'cname': 'Information Systems Senior Project II', 'fall': False, 'spring': True, 'summer': False,'comp_sci' : False, 'data_sci' : False, 'info_sci' : True, 'info_tech' : False, 'info_sys' : True, 'communication': False, 'humanities' : False, 'social_sci': False, 'math_stats' : False, 'science' : False, 'completed': False, 'credit_hrs': 3, 'description': 'The second of a two-course senior project on systems development with a significant laboratory component. Students will design, implement, and deploy a prototype information system in the context of a project team environment employing relevant systems development life cycle methodologies.'},
    
    {'class_id': 'CGS 1100', 'cname': 'Computer Applications for Business', 'fall': True, 'spring': True, 'summer': True,'comp_sci' : False, 'data_sci' : False, 'info_sci' : True, 'info_tech' : True, 'info_sys' : True, 'communication': False, 'humanities' : False, 'social_sci': False, 'math_stats' : False, 'science' : False, 'completed': False, 'credit_hrs': 3, 'description': 'This course provides an introduction to the fundamentals of personal computing for business majors and other non-computer science majors. Topics include the Windows operating system, word processing, spreadsheets, database, presentation aids, internet, e-mail and related areas. Students may not receive credit for CGS1100 and also for CGS1570.'},
    
    {'class_id': 'CIS 4360', 'cname': 'Introduction to Computer Security', 'fall': False, 'spring': True, 'summer': False ,'comp_sci' : False, 'data_sci' : False, 'info_sci' : False, 'info_tech' : True, 'info_sys' : False, 'communication': False, 'humanities' : False, 'social_sci': False, 'math_stats' : False, 'science' : False, 'completed': False, 'credit_hrs': 3, 'description': 'This course presents basic concepts and principles of information security, and the fundamental approaches to secure computers and networks. Main topics include security basics, security management, risk assessment, software security, cryptography algorithms and protocols, and network authentication.'},
    
    {'class_id': 'CIS 3526', 'cname': 'IT Project Management', 'fall': True, 'spring': True, 'summer': True,'comp_sci' : False, 'data_sci' : False, 'info_sci' : False, 'info_tech' : True, 'info_sys' : False, 'completed': False, 'communication': False, 'humanities' : False, 'social_sci': False, 'math_stats' : False, 'science' : False, 'credit_hrs': 3, 'description': 'This course introduces todays best practices in information technology project management. Students are challenged to incrementally create mock project plans and change requests to demonstrate comprehension of scope, time, cost, quality, human resources, communications, risk, procurement and stakeholder management techniques to successfully execute projects. Projects are a group assignment so students leverage their combined interests and knowledge in computer science, information science, information systems, and information technology to imagineer their projects. Formation of project change requests will require creative and analytical thinking to resolve challenges unique to the design, implementation, configuration and maintenance of IT infrastructures and/or software programs. Students who pass this course are eligible to pursue the Associate of Project Management certification (CAPM), an internationally recognized credential in the project management field.'},

    {'class_id': 'COP 4640', 'cname': 'Operating Systems Environments', 'fall': True, 'spring': False, 'summer': False,'comp_sci' : False, 'data_sci' : False, 'info_sci' : False, 'info_tech' : True, 'info_sys' : False, 'communication': False, 'humanities' : False, 'social_sci': False, 'math_stats' : False, 'science' : False, 'completed': False, 'credit_hrs': 3, 'description': 'An introduction to operating systems from theoretical and applied points of view. Topics include operating system configuration, characteristics, and evaluation. The course will explore operating system theory and development using case studies of common operating systems. Students will complete laboratory assignments using the Linux operating system.'},

    {'class_id': 'CIS 4325', 'cname': 'Introduction to Systems Administration', 'fall': False, 'spring': True, 'summer': False,'comp_sci' : False, 'data_sci' : False, 'info_sci' : False, 'info_tech' : True, 'info_sys' : False, 'communication': False, 'humanities' : False, 'social_sci': False, 'math_stats' : False, 'science' : False, 'completed': False, 'credit_hrs': 3, 'description': 'Responsibilities of a Systems Administrator in the world of IT. Topics covered will include: desktop management, servers, services; processes; file systems; user management; backups; disaster recovery; logging; networking; DNS; NFS; email; security; web hosting; software installation, maintenance, and upgrades; printing; performance analysis; policies; and ethics.'},

    {'class_id': 'CNT 4406', 'cname': 'Network Security and Management', 'fall': False, 'spring': True, 'summer': False,'comp_sci' : False, 'data_sci' : False, 'info_sci' : False, 'info_tech' : True, 'info_sys' : False, 'communication': False, 'humanities' : False, 'social_sci': False, 'math_stats' : False, 'science' : False, 'completed': False, 'credit_hrs': 3, 'description': 'In this course, students will identify and analyze user needs and take them into account in the selection, creation, integration, evaluation, and administration of secure computer systems. The course would focus on issues related to the management and security of various network topologies. The use of cryptographic algorithms in the design and implementation of network security protocols will be covered. Various forms of security attacks will be detected, analyzed, and mitigated.'},

    {'class_id': 'CEN 4083', 'cname': 'Introduction to Cloud Computing', 'fall': False, 'spring': True, 'summer': False,'comp_sci' : False, 'data_sci' : False, 'info_sci' : False, 'info_tech' : True, 'info_sys' : False, 'communication': False, 'humanities' : False, 'social_sci': False, 'math_stats' : False, 'science' : False, 'completed': False, 'credit_hrs': 3, 'description': 'The adoption of cloud computing services continues to grow across a variety of organizations and in many domains. Students will be exposed to the current practices in cloud computing. Topics may include cloud service models such as Infrastructure as a Service (IaaS), Platform as a Service (PaaS), Software as a Service (SaaS), virtualization, cloud architectures, motivating factors, benefits and challenges of the cloud, cloud storage, performance and systems issues, disaster recovery, federated clouds, hypervisor CPU and memory management, data centers, and cloud security. Course work may include homework assignments, presentations, and projects that will provide exposure to major cloud services such as Amazon Web Services (AWS) and/or Google Compute Engine (GCE).'},

    {'class_id': 'CIS 4364', 'cname': 'Intrusion Detection', 'fall': True, 'spring': False, 'summer': False,'comp_sci' : False, 'data_sci' : False, 'info_sci' : False, 'info_tech' : True, 'info_sys' : False, 'communication': False, 'humanities' : False, 'social_sci': False, 'math_stats' : False, 'science' : False, 'completed': False, 'credit_hrs': 3, 'description': 'This course explores the use of intrusion detection systems (IDS) as part of an organization''s overall security posture. A variety of approaches, models, and algorithms along with the practical concerns of deploying IDS in an enterprise environment will be discussed. Topics include the history of IDS, anomaly and misuse detection for both host and network environments, policy and legal issues surrounding the use of IDS, how IDS can complement host and network security, and current research topics.'},
    
    {'class_id': 'CIS 4366', 'cname': 'Computer Forensics', 'fall': True, 'spring': False, 'summer': False, 'comp_sci' : False, 'data_sci' : False, 'info_sci' : False, 'info_tech' : True, 'info_sys' : False, 'communication': False, 'humanities' : False, 'social_sci': False, 'math_stats' : False, 'science' : False, 'completed': False, 'credit_hrs': 3, 'description': 'Topics in this course will include computer system data recovery with a particular emphasis on computer evidence handling and computer crime detection. The students will use and develop computer software tools to reboot suspect computers, detect evidence of computer crime, and preserve that evidence for later use. Students will be trained to recover data from simulated crime environments.'},

    {'class_id': 'CAP 4770', 'cname': 'Data Mining', 'fall': True, 'spring': False, 'summer': False, 'comp_sci' : False, 'data_sci' : True, 'info_sci' : False, 'info_tech' : False, 'info_sys' : False, 'communication': False, 'humanities' : False, 'social_sci': False, 'math_stats' : False, 'science' : False, 'completed': False, 'credit_hrs': 3, 'description': 'This course covers methods and systems for mining varied data and discovering knowledge from data. The course will expose students to concepts and techniques of data mining, including characterization and comparison, association rules mining, classification and prediction, and mining complex types of data. Students will also examine applications and trends in data mining.'},

    {'class_id': 'ISM 4011', 'cname': 'Introduction to Management Information Systems', 'fall': True, 'spring': True, 'summer': True, 'comp_sci' : False, 'data_sci' : False, 'info_sci' : False, 'info_tech' : False, 'info_sys' : True, 'communication': False, 'humanities' : False, 'social_sci': False, 'math_stats' : False, 'science' : False, 'completed': False, 'credit_hrs': 3, 'description': 'This course will cover the fundamentals of management information systems with an emphasis on the relationships of MIS and data processing to decision-making in modern organizations.'},

    {'class_id': 'MAN 3025', 'cname': 'Principles of Management', 'fall': True, 'spring': True, 'summer': True, 'comp_sci' : False, 'data_sci' : False, 'info_sci' : False, 'info_tech' : False, 'info_sys' : True, 'communication': False, 'humanities' : False, 'social_sci': False, 'math_stats' : False, 'science' : False, 'completed': False, 'credit_hrs': 3, 'description': 'This course covers fundamentals of management which permeate organizations; including introductory studies of administrative structure, the organizational environment, and managerial functions and processes.'},

    {'class_id': 'FIN 3403', 'cname': 'Financial Management', 'fall': True, 'spring': True, 'summer': True, 'comp_sci' : False, 'data_sci' : False, 'info_sci' : False, 'info_tech' : False, 'info_sys' : True, 'communication': False, 'humanities' : False, 'social_sci': False, 'math_stats' : False, 'science' : False, 'completed': False, 'credit_hrs': 3, 'description': 'This course focuses on management techniques for and considerations in determining short-term, intermediate-term, and long-term financial needs. Sources of funds available to management and the relevant financial instruments will be examined.'},

    {'class_id': 'ECO 2013', 'cname': 'Principles of Macroeconomics', 'fall': True, 'spring': True, 'summer': True, 'comp_sci' : False, 'data_sci' : False, 'info_sci' : False, 'info_tech' : False, 'info_sys' : True, 'communication': False, 'humanities' : False, 'social_sci': True, 'math_stats' : False, 'science' : False, 'completed': False, 'credit_hrs': 3, 'description': 'Introduction to the theory of income determination and national income accounting. Analysis of the use of monetary and fiscal policy to accomplish the goals of full employment, economic growth and price stability. Cannot be used to satisfy upper-level requirements for a degree in business administration and economics. Normally offered each term.'},

    {'class_id': 'ECO 2032', 'cname': 'Intermediate Macroeconomics', 'fall': True, 'spring': True, 'summer': True, 'comp_sci' : False, 'data_sci' : False, 'info_sci' : False, 'info_tech' : False, 'info_sys' : True, 'communication': False, 'humanities' : False, 'social_sci': False, 'math_stats' : False, 'science' : False, 'completed': False, 'credit_hrs': 3, 'description': 'This course analyzes aggregate economic activity and growth, focusing on national economic goals and policies for their attainment.'},

    {'class_id': 'ACG 2021', 'cname': 'Principles of Financial Accounting', 'fall': True, 'spring': True, 'summer': True, 'comp_sci' : False, 'data_sci' : False, 'info_sci' : False, 'info_tech' : False, 'info_sys' : True, 'communication': False, 'humanities' : False, 'social_sci': False, 'math_stats' : False, 'science' : False, 'completed': False, 'credit_hrs': 3, 'description': 'This course is a conceptual introduction to financial accounting. In this course, primary emphasis is placed on income measurement and the interpretation of conventional financial statements.'},
    
    {'class_id': 'ACG 2071', 'cname': 'Principles of Managerial Accounting', 'fall': True, 'spring': True, 'summer': True, 'comp_sci' : False, 'data_sci' : False, 'info_sci' : False, 'info_tech' : False, 'info_sys' : True, 'communication': False, 'humanities' : False, 'social_sci': False, 'math_stats' : False, 'science' : False, 'completed': False, 'credit_hrs': 3, 'description': 'This course is the conceptual introduction to managerial accounting. The material covers accounting for cost reporting and control, reports, statements, and analytical tools used by management.'},

    {'class_id': 'MAC 2233', 'cname': 'Calculus for Business', 'fall': True, 'spring': True, 'summer': True, 'comp_sci' : False, 'data_sci' : False, 'info_sci' : True, 'info_tech' : True, 'info_sys' : True, 'communication': False, 'humanities' : False, 'social_sci': False, 'math_stats' : True, 'science' : False, 'completed': False, 'credit_hrs': 3, 'description': 'Topics in differential and integral calculus with applications.'},

    {'class_id': 'STA 2023', 'cname': 'Elementary Statistics for Business', 'fall': True, 'spring': True, 'summer': True, 'comp_sci' : False, 'data_sci' : False, 'info_sci' : True, 'info_tech' : True, 'info_sys' : True, 'communication': False, 'humanities' : False, 'social_sci': False, 'math_stats' : True, 'science' : False, 'completed': False, 'credit_hrs': 3, 'description': 'his course is an introduction to descriptive data analysis, probability, statistical distributions, confidence intervals, testing of hypotheses, regression, and correlation. Topics selected to emphasize applications in a business environment.'},

    {'class_id': 'MAC 2311', 'cname': 'Calculus I', 'fall': True, 'spring': True, 'summer': True, 'comp_sci' : True, 'data_sci' : True, 'info_sci' : False, 'info_tech' : False, 'info_sys' : False, 'communication': False, 'humanities' : False, 'social_sci': False, 'math_stats' : True, 'science' : False, 'completed': False, 'credit_hrs': 4, 'description': 'This course examines the notions of limit, continuity and derivatives of functions of one variable. The course explores differentiation rules for algebraic, trigonometric, exponential and logarithmic functions. The course discusses applications of differential calculus, such as related rates problems, curve sketching, and optimization. The course also introduces students to definite and indefinite integrals and the Fundamental Theorem of Calculus.'},

    {'class_id': 'MAC 2312', 'cname': 'Calculus II', 'fall': True, 'spring': True, 'summer': True, 'comp_sci' : True, 'data_sci' : True, 'info_sci' : False, 'info_tech' : False, 'info_sys' : False, 'communication': False, 'humanities' : False, 'social_sci': False, 'math_stats' : True, 'science' : False, 'completed': False, 'credit_hrs': 4, 'description': 'This course continues the study of definite and indefinite integrals, and the Fundamental Theorem of Calculus begun in MAC 2311. The course presents various integration techniques and their applications, convergence of sequences and series, as well as power series and Taylor series of a function of one variable.'},

    {'class_id': 'PHY 2048C', 'cname': 'Calculus-based Physics I', 'fall': True, 'spring': True, 'summer': True, 'comp_sci' : True, 'data_sci' : False, 'info_sci' : False, 'info_tech' : False, 'info_sys' : False, 'communication': False, 'humanities' : False, 'social_sci': False, 'math_stats' : False, 'science' : True, 'completed': False, 'credit_hrs': 4, 'description': ''},

    {'class_id': 'PHY 2049', 'cname': 'Calculus-based Physics II', 'fall': True, 'spring': True, 'summer': True, 'comp_sci' : True, 'data_sci' : False, 'info_sci' : False, 'info_tech' : False, 'info_sys' : False, 'communication': False, 'humanities' : False, 'social_sci': False, 'math_stats' : False, 'science' : True, 'completed': False, 'credit_hrs': 3, 'description': 'his course is a continuation of PHY 2048 or PHY 2048C with emphasis on electricity, magnetism and light. This course will be three hours of lecture.'},

    {'class_id': 'PHY 2049L', 'cname': 'Calculus-based Physics II Lab', 'fall': True, 'spring': True, 'summer': False, 'comp_sci' : True, 'data_sci' : False, 'info_sci' : False, 'info_tech' : False, 'info_sys' : False, 'communication': False, 'humanities' : False, 'social_sci': False, 'math_stats' : False, 'science' : True, 'completed': False, 'credit_hrs': 1, 'description': 'This course is the laboratory course that accompanies the PHY 2049 or PHY 2042 courses. This course will be three hours of laboratory.'},
    
    {'class_id': 'STA 3032', 'cname': 'Probability and Statistics for Engineers', 'fall': True, 'spring': True, 'summer': True, 'comp_sci' : True, 'data_sci' : False, 'info_sci' : False, 'info_tech' : False, 'info_sys' : False, 'communication': False, 'humanities' : False, 'social_sci': False, 'math_stats' : False, 'science' : False, 'completed': False, 'credit_hrs': 3, 'description': 'This course is a survey of the basic concepts in probability and statistics with applications in electrical, mechanical, and civil engineering. Topics include probability, common discrete and continuous probability distributions, estimation and hypothesis testing, and simple regression.'},

    {'class_id': 'MAS 3105', 'cname': 'Linear Algebra', 'fall': True, 'spring': True, 'summer': True, 'comp_sci' : True, 'data_sci' : True, 'info_sci' : False, 'info_tech' : False, 'info_sys' : False, 'communication': False, 'humanities' : False, 'social_sci': False, 'math_stats' : False, 'science' : False, 'completed': False, 'credit_hrs': 4, 'description': 'This course covers matrix algebra, Gaussian elimination, determinants, Euclidean spaces, linear transformations, eigenvalues, eigenvectors, and vector spaces.'},

    {'class_id': 'STA 4321', 'cname': 'Probability and Statistics', 'fall': True, 'spring': True, 'summer': True, 'comp_sci' : False, 'data_sci' : True, 'info_sci' : False, 'info_tech' : False, 'info_sys' : False, 'communication': False, 'humanities' : False, 'social_sci': False, 'math_stats' : False, 'science' : False, 'completed': False, 'credit_hrs': 4, 'description': 'This course will cover basic probability principles, random variables and univariate probability distributions, moments and an introduction to moment generating functions, introduction to sampling distributions and the Central Limit Theorem, and introduction to interval estimation and hypothesis testing.'},

    {'class_id': 'STA 3163', 'cname': 'Statistical Methods I', 'fall': True, 'spring': False, 'summer': False, 'comp_sci' : False, 'data_sci' : True, 'info_sci' : False, 'info_tech' : False, 'info_sys' : False, 'communication': False, 'humanities' : False, 'social_sci': False, 'math_stats' : False, 'science' : False, 'completed': False, 'credit_hrs': 4, 'description': 'This is the first in a two-term sequence in applied statistical methods. This course focuses on descriptive and inferential statistics for means and proportions in one and two groups, simple linear regression with its diagnostics, and the one-way analysis of variance. The course incorporates technology and uses SAS for analysis of statistical data.'},

    {'class_id': 'STA 3164', 'cname': 'Statistical Methods II', 'fall': False, 'spring': True, 'summer': False, 'comp_sci' : False, 'data_sci' : True, 'info_sci' : False, 'info_tech' : False, 'info_sys' : False, 'communication': False, 'humanities' : False, 'social_sci': False, 'math_stats' : False, 'science' : False, 'completed': False, 'credit_hrs': 3, 'description': 'This is the second in a two-term sequence in applied statistical methods. In this course, the focus is on more complex data models such as multiple regression, the higher-order analysis of variance, and logistic regression. Data analysis is carried out using the SAS program.'},

    {'class_id': 'ENC 2210', 'cname': 'Technical Writing', 'fall': True, 'spring': True, 'summer': True, 'comp_sci' : False, 'data_sci' : True, 'info_sci' : False, 'info_tech' : False, 'info_sys' : False, 'communication': True, 'humanities' : False, 'social_sci': False, 'math_stats' : False, 'science' : False, 'completed': False, 'credit_hrs': 3, 'description': 'This course will introduce students to scientific, technical, and professional writing with a focus on practical information about communicating in different workplace environments and professional/technical discourse communities. Students will analyze rhetorical situations and issues (of audience, organization, visual design, style, and the material production of documents) common to different scientific, technical, and professional writing genres, including emails, letters, resumes, memos, reports (progress, lab, etc.), proposals, technical descriptions, technical definitions, and technical manuals.'},

    {'class_id': 'STA 4504', 'cname': 'Categorical Data Analysis', 'fall': True, 'spring': True, 'summer': True, 'comp_sci' : False, 'data_sci' : True, 'info_sci' : False, 'info_tech' : False, 'info_sys' : False, 'communication': False, 'humanities' : False, 'social_sci': False, 'math_stats' : False, 'science' : False, 'completed': False, 'credit_hrs': 3, 'description': 'The Categorical Data course is an introduction to the methods used to analyze data that are categorical rather than continuous in nature. The topics include description and inference using proportions and odds ratios, contingency tables, Poisson regression, logistic regression, and multi-category logit models.'},

    {'class_id': 'COT 4560', 'cname': 'Applied Graphg Theory', 'fall': True, 'spring': True, 'summer': True, 'comp_sci' : False, 'data_sci' : True, 'info_sci' : False, 'info_tech' : False, 'info_sys' : False, 'communication': False, 'humanities' : False, 'social_sci': False, 'math_stats' : False, 'science' : False, 'completed': False, 'credit_hrs': 3, 'description': 'Students in this course will study classical graph theory, its applications in computing and modeling real-word phenomena, and graph algorithms.'},

    {'class_id': 'CIS 4900', 'cname': 'Directed Independent Study', 'fall': True, 'spring': True, 'summer': True, 'comp_sci' : False, 'data_sci' : True, 'info_sci' : False, 'info_tech' : False, 'info_sys' : False, 'communication': False, 'humanities' : False, 'social_sci': False, 'math_stats' : False, 'science' : False, 'completed': False, 'credit_hrs': 3, 'description': 'This course is reserved for senior level computing and information science students, on topics supportive of the students overall program.'},

    {'class_id': 'SPC 4064', 'cname': 'Public Speaking for Professionals', 'fall': True, 'spring': True, 'summer': True, 'comp_sci' : True, 'data_sci' : True, 'info_sci' : True, 'info_tech' : True, 'info_sys' : True, 'communication': False, 'humanities' : False, 'social_sci': False, 'math_stats' : False, 'science' : False, 'completed': False, 'credit_hrs': 3, 'description': 'This course is reserved for senior level computing and information science students, on topics supportive of the students overall program.'},

    {'class_id': 'MAJ 0001', 'cname': 'Major Elective I', 'fall': True, 'spring': True, 'summer': True, 'comp_sci' : True, 'data_sci' : True, 'info_sci' : True, 'info_tech' : True, 'info_sys' : True, 'communication': False, 'humanities' : False, 'social_sci': False, 'math_stats' : False, 'science' : False, 'completed': False, 'credit_hrs': 3, 'description': 'Select any upper-level(3XXX or 4XXX) Computing course not used to fulfill other requirements. This includes any course starting with the following: CAP, CDA, CEN, CIS, CNT, COP, or, COT'},

    {'class_id': 'MAJ 0002', 'cname': 'Major Elective II', 'fall': True, 'spring': True, 'summer': True, 'comp_sci' : True, 'data_sci' : True, 'info_sci' : True, 'info_tech' : True, 'info_sys' : True, 'communication': False, 'humanities' : False, 'social_sci': False, 'math_stats' : False, 'science' : False, 'completed': False, 'credit_hrs': 3, 'description': 'Select any upper-level(3XXX or 4XXX) Computing course not used to fulfill other requirements. This includes any course starting with the following: CAP, CDA, CEN, CIS, CNT, COP, or, COT'},

    {'class_id': 'MAJ 0003', 'cname': 'Major Elective III', 'fall': True, 'spring': True, 'summer': True, 'comp_sci' : True, 'data_sci' : True, 'info_sci' : True, 'info_tech' : True, 'info_sys' : True, 'communication': False, 'humanities' : False, 'social_sci': False, 'math_stats' : False, 'science' : False, 'completed': False, 'credit_hrs': 3, 'description': 'Select any upper-level(3XXX or 4XXX) Computing course not used to fulfill other requirements. This includes any course starting with the following: CAP, CDA, CEN, CIS, CNT, COP, or, COT'},

    #--------------------------------------------------------------------------------------------General education classes
    #Part A of General Education Requirements
    #Communications Group 1
    {'class_id' : 'ENC 1101', 'cname' : '(GW) Writing for Audeience and Purpose', 'fall': True, 'spring': True, 'summer': True, 'comp_sci' : False, 'data_sci' : False, 'info_sci' : False, 'info_tech' : False, 'info_sys' : False, 'communication': True, 'humanities' : False, 'social_sci': False, 'math_stats' : False, 'science' : False, 'completed' : False, 'credit_hrs' : 3, 'description' : 'This course will introduce students to common textual issues surrounding audience and purpose to prepare them for the different kinds of texts they will encounter in upper-level academic courses as well as professional settings.Gordon Rule English credit.'},

    #Humanties Group 2   
    {'class_id' : 'ARH 2000', 'cname' : 'Art Appreciation', 'fall': True, 'spring': True, 'summer': True, 'comp_sci' : False, 'data_sci' : False, 'info_sci' : False, 'info_tech' : False, 'info_sys' : False, 'communication': False, 'humanities' : True, 'social_sci': False, 'math_stats' : False, 'science' : False, 'completed' : False, 'credit_hrs' : 3, 'description' : 'This course includes the study of visual elements, design principles, various techniques and media. Examples of Western painting, sculpture and architecture from prehistoric to present times will be examined. Local museum excursions are required.'},

    {'class_id' : 'LIT 2000', 'cname' : '(GW) Introduction to Literature', 'fall': True, 'spring': True, 'summer': True, 'comp_sci' : False, 'data_sci' : False, 'info_sci' : False, 'info_tech' : False, 'info_sys' : False, 'communication': False, 'humanities' : True, 'social_sci': False, 'math_stats' : False, 'science' : False, 'completed' : False, 'credit_hrs' : 3, 'description' : 'Prerequisite:  ENC 1101; The course will introduce students to writing about literature with a focus on the close reading, critical analysis, and informed appreciation of different kinds of literary texts. Gordon Rule English credit.'},

    {'class_id' : 'MUL 2010', 'cname' : '(GW) Introduction to Music Literature', 'fall': True, 'spring': True, 'summer': True, 'comp_sci' : False, 'data_sci' : False, 'info_sci' : False, 'info_tech' : False, 'info_sys' : False, 'communication': False, 'humanities' : True, 'social_sci': False, 'math_stats' : False, 'science' : False, 'completed' : False, 'credit_hrs' : 3, 'description' : 'This course examines music and its role in culture: how it both shapes and is shaped by social, political, national, and cultural forces. Examples from art music, popular music, and world music will illustrate music’s connection to life in both historical and contemporary settings. No prior musical training or experience are required for enrollment.'},

    {'class_id' : 'PHI 2010', 'cname' : '(GW) Introduction to Philosophy', 'fall': True, 'spring': True, 'summer': True, 'comp_sci' : False, 'data_sci' : False, 'info_sci' : False, 'info_tech' : False, 'info_sys' : False, 'communication': False, 'humanities' : True, 'social_sci': False, 'math_stats' : False, 'science' : False, 'completed' : False, 'credit_hrs' : 3, 'description' : 'An introduction to the rudiments of philosophical thinking, which is designed to clarify the differences between philosophy and other human activities such as science and religion. The course will introduce students to a range of philosophical problems and methods. Gordon Rule Additional Writing credit.'},

    {'class_id' : 'THE 2000', 'cname' : 'Theater Appreciation', 'fall': True, 'spring': True, 'summer': True, 'comp_sci' : False, 'data_sci' : False, 'info_sci' : False, 'info_tech' : False, 'info_sys' : False, 'communication': False, 'humanities' : True, 'social_sci': False, 'math_stats' : False, 'science' : False, 'completed' : False, 'credit_hrs' : 3, 'description' : 'This course is for students interested in understanding and appreciating one of the oldest art forms in the world. For thousands of years, humans have put on masks and adopted personas and behaved as if they were different from the people they are. Why? Why have they felt the need to pretend to be who they are not, to express feelings that are not really their own, and to direct their bodies to act out stories in front of spectators, stories in which they come into conflict with others? In order to address these and related questions, students will read plays, analyze scripts, and attend and write about local productions. They may also complete a group project in a live theater. No acting experience is required. The course can be applied to Category C for non-applied fine arts General Education credit.'},

    #Social Sciences Group 3
    {'class_id' : 'AMH 2020', 'cname' : 'United States History Since 1877', 'fall': True, 'spring': True, 'summer': True, 'comp_sci' : False, 'data_sci' : False, 'info_sci' : False, 'info_tech' : False, 'info_sys' : False, 'communication': False, 'humanities' : False, 'social_sci': True, 'math_stats' : False, 'science' : False, 'completed' : False, 'credit_hrs' : 3, 'description' : 'A history of the United States since 1877 emphasizing industrialization and urbanization, the Progressive period, the New Deal, post-World War II domestic reform and the emergence of the U.S. as a world power.'},

    {'class_id' : 'ANT 2000', 'cname' : 'Introduciton to Anthropology', 'fall': True, 'spring': True, 'summer': True, 'comp_sci' : False, 'data_sci' : False, 'info_sci' : False, 'info_tech' : False, 'info_sys' : False, 'communication': False, 'humanities' : False, 'social_sci': True, 'math_stats' : False, 'science' : False, 'completed' : False, 'credit_hrs' : 3, 'description' : 'An introduction to the critical issues in anthropology. The major subfields of archaeology, physical anthropology, linguistics, and cultural anthropology are examined for an understanding of contemporary and past cultural issues such as the rise of civilization, origins of language, and the roots of social inequality.'},

    {'class_id' : 'POS 2041', 'cname' : 'Introduction to American Government', 'fall': True, 'spring': True, 'summer': True, 'comp_sci' : False, 'data_sci' : False, 'info_sci' : False, 'info_tech' : False, 'info_sys' : False, 'communication': False, 'humanities' : False, 'social_sci': True, 'math_stats' : False, 'science' : False, 'completed' : False, 'credit_hrs' : 3, 'description' : 'This course provides a broad look at government in the U.S., introducing major institutions and participants and considering various explanations of why our political system behaves as it does. The course reviews governmental response to major issues to illustrate both the power and limitations of our system of government.'},

    {'class_id' : 'PSY 2012', 'cname' : 'Introduction to Psychology', 'fall': True, 'spring': True, 'summer': True, 'comp_sci' : False, 'data_sci' : False, 'info_sci' : False, 'info_tech' : False, 'info_sys' : False, 'communication': False, 'humanities' : False, 'social_sci': True, 'math_stats' : False, 'science' : False, 'completed' : False, 'credit_hrs' : 3, 'description' : 'This course is an introduction to the scientific study of human and animal behavior. The principles, theories and methods of psychology will be surveyed in the context of topics central to the development and present status of the discipline.'},

    {'class_id' : 'SYG 2000', 'cname' : 'Introduction to Sociology', 'fall': True, 'spring': True, 'summer': True, 'comp_sci' : False, 'data_sci' : False, 'info_sci' : False, 'info_tech' : False, 'info_sys' : False, 'communication': False, 'humanities' : False, 'social_sci': True, 'math_stats' : False, 'science' : False, 'completed' : False, 'credit_hrs' : 3, 'description' : 'A study of sociological concepts essential for an understanding of individual, society and social structure. General concepts which integrate the field are considered so that more specialized courses may be understood in context.'},

    #Mathematics and Stastics Group 4
    {'class_id' : 'MAC 1105', 'cname' : 'College Algebra', 'fall': True, 'spring': True, 'summer': True, 'comp_sci' : False, 'data_sci' : False, 'info_sci' : False, 'info_tech' : False, 'info_sys' : False, 'communication': False, 'humanities' : False, 'social_sci': False, 'math_stats' : True, 'science' : False, 'completed' : False, 'credit_hrs' : 3, 'description' : 'Topics include linear and quadratic functions, systems of equations and inequalities, polynomials, exponentials, logarithms, and applications. Students attend three hours of lecture per week. Students may only earn credit for one of the following: MAC1105, MAC1105C, or MAC1101C. Meets the General Education requirement in Mathematics. Meets the Gordon Rule requirement.'},

    {'class_id' : 'MGF 1106', 'cname' : 'Finite Mathematics', 'fall': True, 'spring': True, 'summer': True, 'comp_sci' : False, 'data_sci' : False, 'info_sci' : False, 'info_tech' : False, 'info_sys' : False, 'communication': False, 'humanities' : False, 'social_sci': False, 'math_stats' : True, 'science' : False, 'completed' : False, 'credit_hrs' : 3, 'description' : 'Prerequisite:  MAT1033; This course is primarily for non-science and non-business majors who need to fulfill the general education math requirement. It presents the study of mathematical concepts that arise in real world applications. Topics may include linear equations and inequalities, matrices and systems of linear equations, counting techniques and elementary probability, game theory with applications, logic, and mathematics of finance.'},

    {'class_id' : 'MGF 1107', 'cname' : 'Explorations of Mathematics', 'fall': True, 'spring': True, 'summer': True, 'comp_sci' : False, 'data_sci' : False, 'info_sci' : False, 'info_tech' : False, 'info_sys' : False, 'communication': False, 'humanities' : False, 'social_sci': False, 'math_stats' : True, 'science' : False, 'completed' : False, 'credit_hrs' : 3, 'description' : 'Prerequisite:  MAT 1033; This course is primarily for non-science and non-business majors who need to fulfill the general education math requirement. This course promotes the appreciation of applied mathematics. MGF1106 Finite Mathematics is not a prerequisite for this course. Topics may include number theory, voting theory, rates of growth, geometry, and graph theory.'},

    #Natural and Physical Sciences Group 5
    {'class_id' : 'AST 2002', 'cname' : 'Discovering Astronomy', 'fall': True, 'spring': True, 'summer': True, 'comp_sci' : False, 'data_sci' : False, 'info_sci' : False, 'info_tech' : False, 'info_sys' : False, 'communication': False, 'humanities' : False, 'social_sci': False, 'math_stats' : False, 'science' : True, 'completed' : False, 'credit_hrs' : 3, 'description' : 'This course is a survey of current knowledge of the astronomical universe and of how that knowledge has been accumulated. Students will study the solar system, stars, and galaxies, and will review contemporary research and exploration. This course will include occasional observing sessions and there will be three hours of lecture each week.'},

    {'class_id' : 'BSC 1005', 'cname' : 'Principles of Biology', 'fall': True, 'spring': True, 'summer': True, 'comp_sci' : False, 'data_sci' : False, 'info_sci' : False, 'info_tech' : False, 'info_sys' : False, 'communication': False, 'humanities' : False, 'social_sci': False, 'math_stats' : False, 'science' : True, 'completed' : False, 'credit_hrs' : 3, 'description' : 'Co-requisite: BSC1005L; This course is designed to introduce students to the science of life. This survey course will cover a wide range of topics from the molecular components of the cell to the interaction of organisms with their environment. The goal of this course is to familiarize students with diverse components of life and to introduce the major areas of study within the discipline.'},

    {'class_id' : 'BSC 1010C', 'cname' : 'General Biology I', 'fall': True, 'spring': True, 'summer': True, 'comp_sci' : False, 'data_sci' : False, 'info_sci' : False, 'info_tech' : False, 'info_sys' : False, 'communication': False, 'humanities' : False, 'social_sci': False, 'math_stats' : False, 'science' : True, 'completed' : False, 'credit_hrs' : 3, 'description' : 'An introduction to biology with emphasis on the cellular level. Three hours lecture, four hours laboratory. (A laboratory fee of $51.93 will be assessed.)'},

    {'class_id' : 'BSC 2085C', 'cname' : 'Human Anatomy and Physiology', 'fall': True, 'spring': True, 'summer': True, 'comp_sci' : False, 'data_sci' : False, 'info_sci' : False, 'info_tech' : False, 'info_sys' : False, 'communication': False, 'humanities' : False, 'social_sci': False, 'math_stats' : False, 'science' : True, 'completed' : False, 'credit_hrs' : 3, 'description' : 'Prerequisite:  BSC 1010C; This course includes units concerning the organization of the human body, support and movement, the nervous system and special senses, and the endocrine system. The laboratory involves dissection of preserved animals. (A course fee of $51.93 will be assessed.)'},

    {'class_id' : 'CHM 1020', 'cname' : 'Discovering Chemistry', 'fall': True, 'spring': True, 'summer': True, 'comp_sci' : False, 'data_sci' : False, 'info_sci' : False, 'info_tech' : False, 'info_sys' : False, 'communication': False, 'humanities' : False, 'social_sci': False, 'math_stats' : False, 'science' : True, 'completed' : False, 'credit_hrs' : 3, 'description' : 'This course introduces basic chemical principles without an extensive use of mathematics and illustrates them with applications in health, energy, food, and the environment. This course strives to show chemistry as a human endeavor that provides insight into the natural world and informs our decisions as citizens and consumers. Specific topics may vary by semester. This course is designed as a course for students that wish to fulfill the general education natural science requirement with chemistry and who will take no further chemistry courses. This course is not a preparatory course for CHM 2045.'},

    {'class_id' : 'CHM 2045', 'cname' : 'General Chemistry I', 'fall': True, 'spring': True, 'summer': True, 'comp_sci' : False, 'data_sci' : False, 'info_sci' : False, 'info_tech' : False, 'info_sys' : False, 'communication': False, 'humanities' : False, 'social_sci': False, 'math_stats' : False, 'science' : True, 'completed' : False, 'credit_hrs' : 3, 'description' : 'Prerequisite:  CHM 1025 or qualifying score on chemistry placement assessment and MAC 1105; Co-requisite: CHM 2045L; The course is the first semester of a two semester sequence, and includes topics such as stoichiometry, atomic structure, chemical bonding, solutions and their properties, descriptive chemistry of selected elements, and gases.'},

    {'class_id' : 'ESC 2000', 'cname' : 'Earth Science', 'fall': True, 'spring': True, 'summer': True, 'comp_sci' : False, 'data_sci' : False, 'info_sci' : False, 'info_tech' : False, 'info_sys' : False, 'communication': False, 'humanities' : False, 'social_sci': False, 'math_stats' : False, 'science' : True, 'completed' : False, 'credit_hrs' : 3, 'description' : 'This course is an introduction to the Earth as a system including the lithosphere, atmosphere, and the hydrosphere. Topics for discussion will include the formation of the Earth and the evolution of its landscape, the atmosphere and principles of weather and climate, the dynamic ocean, comparison with other bodies in the Solar System and human impact on the Earth systems.'},

    {'class_id' : 'EVR X001', 'cname' : 'Introduction to Environmental Science', 'fall': True, 'spring': True, 'summer': True, 'comp_sci' : False, 'data_sci' : False, 'info_sci' : False, 'info_tech' : False, 'info_sys' : False, 'communication': False, 'humanities' : False, 'social_sci': False, 'math_stats' : False, 'science' : True, 'completed' : False, 'credit_hrs' : 3, 'description' : ''},

    {'class_id' : 'PHY 1020', 'cname' : 'Discovering Physics: How things work', 'fall': True, 'spring': True, 'summer': True, 'comp_sci' : False, 'data_sci' : False, 'info_sci' : False, 'info_tech' : False, 'info_sys' : False, 'communication': False, 'humanities' : False, 'social_sci': False, 'math_stats' : False, 'science' : True, 'completed' : False, 'credit_hrs' : 3, 'description' : 'This course will survey and explore fundamental concepts in physics and how these concepts can be used to understand the world around us. Topics covered include force, energy, electricity, magnetism, and the structure of matter. The course will emphasize conceptual understanding rather than mathematical problem solving. This course is not intended for students planning to major in science or engineering.'},

    {'class_id' : 'PHY 2053', 'cname' : 'Algebra-Based Physics I', 'fall': True, 'spring': True, 'summer': True, 'comp_sci' : False, 'data_sci' : False, 'info_sci' : False, 'info_tech' : False, 'info_sys' : False, 'communication': False, 'humanities' : False, 'social_sci': False, 'math_stats' : False, 'science' : True, 'completed' : False, 'credit_hrs' : 3, 'description' : 'Prerequisite:  Either MAC 1105 and MAC 1114 or just MAC 1147; PHY1028; This course is an introduction to mechanics, waves and heat. Calculus is not required in this course. This course will be three hours of lecture.'},

    #Part B of General Education Requirements
    #Writing Effectively (6 Hours)
    {'class_id' : 'ENC 1143', 'cname' : '(GW) Writing with Evidence and Style', 'fall': True, 'spring': True, 'summer': True, 'comp_sci' : False, 'data_sci' : False, 'info_sci' : False, 'info_tech' : False, 'info_sys' : False, 'communication': True, 'humanities' : False, 'social_sci': False, 'math_stats' : False, 'science' : False, 'completed' : False, 'credit_hrs' : 3, 'description' : 'This course will introduce students to common textual issues surrounding evidence-based writing, genre conventions, and citation style considerations to prepare them for the different kinds of texts they will encounter in upper-level academic courses as well as professional settings. Gordon Rule English credit.'},

    {'class_id' : 'IDS 1932', 'cname' : '(GW) Interdisciplinary First Year Writing', 'fall': True, 'spring': True, 'summer': True, 'comp_sci' : False, 'data_sci' : False, 'info_sci' : False, 'info_tech' : False, 'info_sys' : False, 'communication': True, 'humanities' : False, 'social_sci': False, 'math_stats' : False, 'science' : False, 'completed' : False, 'credit_hrs' : 3, 'description' : 'This course is a first-year writing seminar that blends topics, issues, and knowledge from two or more disciplines, including Writing Studies. This course is intended for students interested in topics ranging from history to art to science and technology to business and is designed exclusively for first-year students. Please note: This course will substitute for ENC 1143, so students cannot receive credit for both ENC 1143 and the first year interdisciplinary writing seminar.'},

    {'class_id' : 'ENC 3202', 'cname' : '(GW) Professional Communications for Business', 'fall': True, 'spring': True, 'summer': True, 'comp_sci' : False, 'data_sci' : False, 'info_sci' : False, 'info_tech' : False, 'info_sys' : False, 'communication': True, 'humanities' : False, 'social_sci': False, 'math_stats' : False, 'science' : False, 'completed' : False, 'credit_hrs' : 3, 'description' : 'In this course, students develop the virtues of business communication—practicality, accountability, and reliability. They learn the profession’s language first-hand by reading and researching in business literature. In discussing such texts, evaluating them, and responding in kind through their own presentations and documents, students become more articulate professionals, more insightful thinkers, and more fluent participants in public life. This is a Gordon Writing Rule course.'},

    {'class_id' : 'ENC 3250', 'cname' : '(GW) Professional Communications', 'fall': True, 'spring': True, 'summer': True, 'comp_sci' : False, 'data_sci' : False, 'info_sci' : False, 'info_tech' : False, 'info_sys' : False, 'communication': True, 'humanities' : False, 'social_sci': False, 'math_stats' : False, 'science' : False, 'completed' : False, 'credit_hrs' : 3, 'description' : 'The primary emphasis of technical writing is on the basics of professional communication-research, organization, grammar/mechanics/style. We will also pay attention to the forms of professional communication-letters, memos, and formal and informal reports. Gordon Rule English credit.'},

    #Thinking Critically --------------------------------------here down checked
    {'class_id' : 'AFH 3450', 'cname' : 'South Africa',  'fall': True, 'spring': True, 'summer': True, 'comp_sci' : False, 'data_sci' : False, 'info_sci' : False, 'info_tech' : False, 'info_sys' : False, 'communication': False, 'humanities' : True, 'social_sci': False, 'math_stats' : False, 'science' : False, 'completed' : False, 'credit_hrs' : 3, 'description' : 'This class investigates the origins and development of South Africa from the colonial period in the seventeenth century to the present. The course examines the complex interactions between the myriad groups during different eras of South African history. The class also compares and contrasts the history of race relations in South Africa and the United States.'},

    {'class_id' : 'AMH 3571', 'cname' : 'Introduction to African-American History', 'fall': True, 'spring': True, 'summer': True, 'comp_sci' : False, 'data_sci' : False, 'info_sci' : False, 'info_tech' : False, 'info_sys' : False, 'communication': False, 'humanities' : True, 'social_sci': False, 'math_stats' : False, 'science' : False, 'completed' : False, 'credit_hrs' : 3, 'description' : 'The African-American experience from the colonial period to the Civil War era, from slavery to freedom. Key themes include the evolution of the African-American family and community, and the emancipation and civil rights movements before the 20th century.'},

    {'class_id' : 'AMH 3580', 'cname' : 'American Indian History', 'fall': True, 'spring': True, 'summer': True, 'comp_sci' : False, 'data_sci' : False, 'info_sci' : False, 'info_tech' : False, 'info_sys' : False, 'communication': False, 'humanities' : True, 'social_sci': False, 'math_stats' : False, 'science' : False, 'completed' : False, 'credit_hrs' : 3, 'description' : 'This course examines North American Indian history from the pre-colonial period through the late twentieth century. We focus on understanding how different American Indian nations resisted and responded to the challenges (and opportunities) presented by European colonization, westward expansion, and U.S. federal and state policies. The course studies the diversity of American Indian societies and their experiences, and the historical roots of key issues in American Indian communities today.'},

    {'class_id' : 'ANT 2423', 'cname' : 'Kinship and Family', 'fall': True, 'spring': True, 'summer': True, 'comp_sci' : False, 'data_sci' : False, 'info_sci' : False, 'info_tech' : False, 'info_sys' : False, 'communication': False, 'humanities' : True, 'social_sci': False, 'math_stats' : False, 'science' : False, 'completed' : False, 'credit_hrs' : 3, 'description' : 'This course introduces students to the study of kinship and gender in an anthropological perspective. Topics covered include, but are not restricted to, gender distinctions, body images, descent, inheritance, courtship, love, marriage, family forms, kin networks, and new reproductive technologies. Students will be presented with detailed case studies both within and outside the Euro-American tradition.'},

    {'class_id' : 'ANT 3212', 'cname' : 'Peoples & Cultures of the World', 'fall': True, 'spring': True, 'summer': True, 'comp_sci' : False, 'data_sci' : False, 'info_sci' : False, 'info_tech' : False, 'info_sys' : False, 'communication': False, 'humanities' : True, 'social_sci': False, 'math_stats' : False, 'science' : False, 'completed' : False, 'credit_hrs' : 3, 'description' : 'This course uses a comparative approach to investigative common bonds of culture and the ways in which Homo sapiens elaborate cultural differences. This course uses cross-cultural evidence to investigate some of the fundamental cultural building blocks of kinship, subsistence technology, and political behavior.'},

    {'class_id' : 'ANT 3312', 'cname' : 'North American Indians', 'fall': True, 'spring': True, 'summer': True, 'comp_sci' : False, 'data_sci' : False, 'info_sci' : False, 'info_tech' : False, 'info_sys' : False, 'communication': False, 'humanities' : True, 'social_sci': False, 'math_stats' : False, 'science' : False, 'completed' : False, 'credit_hrs' : 3, 'description' : 'This course examines selected Indian groups from a holistic perspective and compares different cultural complexes. Particular attention will be given to religion, world view, kinship, politics and economic subsistence patterns. A study of aboriginal Indian cultures will be used as a basis for comparison with current American cultures.'},

    {'class_id' : 'ARH 2050', 'cname' : 'Art History Survey I', 'fall': True, 'spring': True, 'summer': True, 'comp_sci' : False, 'data_sci' : False, 'info_sci' : False, 'info_tech' : False, 'info_sys' : False, 'communication': False, 'humanities' : True, 'social_sci': False, 'math_stats' : False, 'science' : False, 'completed' : False, 'credit_hrs' : 3, 'description' : 'This course is a survey of painting, sculpture and architecture from the Paleolithic era through the Medieval period. Monuments will be studied in relation to the cultural contexts of Western civilization.'},

    {'class_id' : 'ARH 2051', 'cname' : 'Art History Survey II', 'fall': True, 'spring': True, 'summer': True, 'comp_sci' : False, 'data_sci' : False, 'info_sci' : False, 'info_tech' : False, 'info_sys' : False, 'communication': False, 'humanities' : True, 'social_sci': False, 'math_stats' : False, 'science' : False, 'completed' : False, 'credit_hrs' : 3, 'description' : 'This course is a survey of European painting, sculpture and architecture from the Renaissance, Baroque, Rococo, and Neoclassical periods to the emergence of modern art including Romanticism, Realism, Impressionism, Expressionism and Cubism.'},

    {'class_id' : 'ASH 3223', 'cname' : 'Middle East', 'fall': True, 'spring': True, 'summer': True, 'comp_sci' : False, 'data_sci' : False, 'info_sci' : False, 'info_tech' : False, 'info_sys' : False, 'communication': False, 'humanities' : True, 'social_sci': False, 'math_stats' : False, 'science' : False, 'completed' : False, 'credit_hrs' : 3, 'description' : 'An introduction to the historical forces shaping the Middle East, such as Islam, nationalism, Westernization, and nation-state building. Topics covered include: Islamic civilization, the Ottoman Empire, the Eastern Question, the Arab awakening, the Iranian Revolution, the Arab-Israeli dispute, and the regional and global repercussions of contemporary issues.'},

    {'class_id' : 'ASH 3440', 'cname' : 'Japanese Civilization', 'fall': True, 'spring': True, 'summer': True, 'comp_sci' : False, 'data_sci' : False, 'info_sci' : False, 'info_tech' : False, 'info_sys' : False, 'communication': False, 'humanities' : True, 'social_sci': False, 'math_stats' : False, 'science' : False, 'completed' : False, 'credit_hrs' : 3, 'description' : 'This course aims to provide the student with an introduction to Japanese history and society. Topics will include Japanese ethnocentrism, religious traditions, historical consciousness, village society, urbanism, family life, education, contemporary politics, Japans economic miracle, consumerism, sports and the arts. We will look at the Japanese as they see themselves.'},

    {'class_id' : 'ASN 2003', 'cname' : 'Introduction to Asia', 'fall': True, 'spring': True, 'summer': True, 'comp_sci' : False, 'data_sci' : False, 'info_sci' : False, 'info_tech' : False, 'info_sys' : False, 'communication': False, 'humanities' : True, 'social_sci': False, 'math_stats' : False, 'science' : False, 'completed' : False, 'credit_hrs' : 3, 'description' : 'An introduction to the history and culture of Asia. In addition to examining selected aspects of Asias past and present, we will also explore the problems of "Orientalism" and the historical standards employed in various chronicles of Asia (required for the minor in Asian studies).'},

    {'class_id' : 'CCJ 2002', 'cname' : 'Crime in America', 'fall': True, 'spring': True, 'summer': True, 'comp_sci' : False, 'data_sci' : False, 'info_sci' : False, 'info_tech' : False, 'info_sys' : False, 'communication': False, 'humanities' : True, 'social_sci': False, 'math_stats' : False, 'science' : False, 'completed' : False, 'credit_hrs' : 3, 'description' : 'This course is an introduction to the study of criminology/criminal justice. The course includes topics on: the crime problem in the U.S.; crime patterns and criminal behaviors; explanations for crime; systems of justice designed to deal with crime and their underlying philosophies; and preventive strategies.'},

    {'class_id' : 'ECO 3701', 'cname' : 'Contemporary International Economic', 'fall': True, 'spring': True, 'summer': True, 'comp_sci' : False, 'data_sci' : False, 'info_sci' : False, 'info_tech' : False, 'info_sys' : False, 'communication': False, 'humanities' : True, 'social_sci': False, 'math_stats' : False, 'science' : False, 'completed' : False, 'credit_hrs' : 3, 'description' : 'This course introduces students to the contours of the global economy through the lenses of contemporary policy discussions and debates. Topics include international trade, migration, global financial flows, economic development, and international economic institutions. Students will critically evaluate a specific example of international economic policy from the point of view of a selected country.'},

    {'class_id' : 'EDF 2085', 'cname' : 'Introduction to Diversity for Educators', 'fall': True, 'spring': True, 'summer': True, 'comp_sci' : False, 'data_sci' : False, 'info_sci' : False, 'info_tech' : False, 'info_sys' : False, 'communication': False, 'humanities' : True, 'social_sci': False, 'math_stats' : False, 'science' : False, 'completed' : False, 'credit_hrs' : 3, 'description' : 'Designed for the prospective educator, this course provides the opportunity to explore issues of diversity, including an understanding of the influence of exceptionalities, culture, family, gender, sexual orientation, socioeconomic status, religion, language of origin, ethnicity, and age upon the educational experience. Students will explore personal attitudes toward diversity and exceptionalities. Students will be provided information on the Florida Educator Accomplished Practices, Sunshine State Standards, and the Professional Educator Competencies. A minimum of 18 hours of field-based experiences working with diverse populations of children and youth in schools or similar settings is required. The experiences should not be conducted via virtual modes of film or Internet. It is highly recommended that this course not be taken concurrently with EDF1005 Introduction to the Teaching Profession.'},

    {'class_id' : 'EEX 3005', 'cname' : 'Introduction to Disabilities', 'fall': True, 'spring': True, 'summer': True, 'comp_sci' : False, 'data_sci' : False, 'info_sci' : False, 'info_tech' : False, 'info_sys' : False, 'communication': False, 'humanities' : True, 'social_sci': False, 'math_stats' : False, 'science' : False, 'completed' : False, 'credit_hrs' : 3, 'description' : 'This course provides an overview of the characteristics and needs of individuals with disabilities, and it is the initial course for students who want to pursue a minor in Disability Services. Students will interact with individuals with disabilities, discuss strengths-based strategies, and learn about typical barriers that individuals with disabilities face in society.'},

    {'class_id' : 'ENG 3613', 'cname' : 'Topics in Disability Studies', 'fall': True, 'spring': True, 'summer': True, 'comp_sci' : False, 'data_sci' : False, 'info_sci' : False, 'info_tech' : False, 'info_sys' : False, 'communication': False, 'humanities' : True, 'social_sci': False, 'math_stats' : False, 'science' : False, 'completed' : False, 'credit_hrs' : 3, 'description' : 'The course will focus on the nature, meaning, and consequences of what it is to be defined as disabled and explore the historical and cultural dynamics of disability. It will primarily address the stereotypes associated with and the experiential aspects of disability as these are deployed in literature, film, television, the arts, and other cultural media. It will address disability rights, legal issues, and public policy as secondary issues. Course may be repeated for a total of 6 credits with different topics.'},

    {'class_id' : 'EUH 3580', 'cname' : 'Russian Thought & Culture', 'fall': True, 'spring': True, 'summer': True, 'comp_sci' : False, 'data_sci' : False, 'info_sci' : False, 'info_tech' : False, 'info_sys' : False, 'communication': False, 'humanities' : True, 'social_sci': False, 'math_stats' : False, 'science' : False, 'completed' : False, 'credit_hrs' : 3, 'description' : ''},

    {'class_id' : 'FIL 2000', 'cname' : 'Film Appreciation', 'fall': True, 'spring': True, 'summer': True, 'comp_sci' : False, 'data_sci' : False, 'info_sci' : False, 'info_tech' : False, 'info_sys' : False, 'communication': False, 'humanities' : True, 'social_sci': False, 'math_stats' : False, 'science' : False, 'completed' : False, 'credit_hrs' : 3, 'description' : 'This course introduces students to film interpretation and analysis by teaching cinematic vocabulary and technique as they have emerged and developed through the history of international cinema.'},

    {'class_id' : 'FIL 4848', 'cname' : 'World Cinema Across Cultures', 'fall': True, 'spring': True, 'summer': True, 'comp_sci' : False, 'data_sci' : False, 'info_sci' : False, 'info_tech' : False, 'info_sys' : False, 'communication': False, 'humanities' : True, 'social_sci': False, 'math_stats' : False, 'science' : False, 'completed' : False, 'credit_hrs' : 3, 'description' : 'Based on a set of films that focus on the situation of the cross-cultural encounter--including tourism, immigration, and transnational romance—this course will provide students with the analytical tools to address three central questions: What does it mean to be “abroad”? What are the pleasures, privileges, and perils of being “lost in translation”? And how does the cinema both reflect and participate in globalization? The principle analytical tools will be drawn from the diverse interdisciplinary fields of cinema and media studies, cultural studies, postcolonial studies, and cultural anthropology.'},

    {'class_id' : 'GEO 2420', 'cname' : 'Cultural Geograph', 'fall': True, 'spring': True, 'summer': True, 'comp_sci' : False, 'data_sci' : False, 'info_sci' : False, 'info_tech' : False, 'info_sys' : False, 'communication': False, 'humanities' : True, 'social_sci': False, 'math_stats' : False, 'science' : False, 'completed' : False, 'credit_hrs' : 3, 'description' : 'This course analyzes the characteristics of human behavior in different cultures throughout the world. The course focuses on the ways diverse cultures organize themselves spatially to adapt to their geographic area. This Cultural Diversity course is offered every term.'},

    {'class_id' : 'HSC 2100', 'cname' : 'Personal and Community Health', 'fall': True, 'spring': True, 'summer': True, 'comp_sci' : False, 'data_sci' : False, 'info_sci' : False, 'info_tech' : False, 'info_sys' : False, 'communication': False, 'humanities' : True, 'social_sci': False, 'math_stats' : False, 'science' : False, 'completed' : False, 'credit_hrs' : 3, 'description' : 'This course examines US health priorities with an emphasis on behavioral and social determinants of health. Material presented will raise levels of awareness and provide information needed to make informed health related choices, encourage attitude change, and develop decision making skills which facilitate healthier lifestyle behaviors.'},

    {'class_id' : 'LAH 3300', 'cname' : 'Latin America', 'fall': True, 'spring': True, 'summer': True, 'comp_sci' : False, 'data_sci' : False, 'info_sci' : False, 'info_tech' : False, 'info_sys' : False, 'communication': False, 'humanities' : True, 'social_sci': False, 'math_stats' : False, 'science' : False, 'completed' : False, 'credit_hrs' : 3, 'description' : 'An examination of recent Latin American history. Special emphasis will be placed upon the roles of the church, landowner, military, middle sector and peasant in the modernizing societies of selected countries.'},

    {'class_id' : 'LDR 3003', 'cname' : 'Introduction to Leadership', 'fall': True, 'spring': True, 'summer': True, 'comp_sci' : False, 'data_sci' : False, 'info_sci' : False, 'info_tech' : False, 'info_sys' : False, 'communication': False, 'humanities' : True, 'social_sci': False, 'math_stats' : False, 'science' : False, 'completed' : False, 'credit_hrs' : 3, 'description' : 'The course introduces participants to the major theories of leadership and their application in personal and professional settings. Participants engage in self-reflective and applied learning activities that allow them to draw upon their personal characteristics and experiences to make connections between class work and their own developing leadership style.'},

    {'class_id' : 'MMC 2701', 'cname' : 'Communicating Across Cultures', 'fall': True, 'spring': True, 'summer': True, 'comp_sci' : False, 'data_sci' : False, 'info_sci' : False, 'info_tech' : False, 'info_sys' : False, 'communication': False, 'humanities' : True, 'social_sci': False, 'math_stats' : False, 'science' : False, 'completed' : False, 'credit_hrs' : 3, 'description' : 'This course will review the issues involved in effective cross-cultural communication, at the levels of both interpersonal communication and communication through the mass media. Students will be encouraged to explore their own cognitive barriers to communicating across cultures and ways to overcome those barriers.'},

    {'class_id' : 'MUH 2012', 'cname' : 'Enjoyment of Music', 'fall': True, 'spring': True, 'summer': True, 'comp_sci' : False, 'data_sci' : False, 'info_sci' : False, 'info_tech' : False, 'info_sys' : False, 'communication': False, 'humanities' : True, 'social_sci': False, 'math_stats' : False, 'science' : False, 'completed' : False, 'credit_hrs' : 3, 'description' : 'An introduction to musical elements, forms, and style periods with emphasis on composers lives, individual styles and representative works. Designed to stimulate the students love of music and to create listening skills. Music will be studied from the Medieval through the 20th century periods.'},

    {'class_id' : 'MUH 2017', 'cname' : 'The History and Appreciation of Rock', 'fall': True, 'spring': True, 'summer': True, 'comp_sci' : False, 'data_sci' : False, 'info_sci' : False, 'info_tech' : False, 'info_sys' : False, 'communication': False, 'humanities' : True, 'social_sci': False, 'math_stats' : False, 'science' : False, 'completed' : False, 'credit_hrs' : 3, 'description' : 'A study of the origins and development of rock and roll music from rhythm and blues, country and western, to current trends in pop and rock. Aural recognition of representative recordings will be required.'},

    {'class_id' : 'MUH 2018', 'cname' : 'Evolution of Jazz', 'fall': True, 'spring': True, 'summer': True, 'comp_sci' : False, 'data_sci' : False, 'info_sci' : False, 'info_tech' : False, 'info_sys' : False, 'communication': False, 'humanities' : True, 'social_sci': False, 'math_stats' : False, 'science' : False, 'completed' : False, 'credit_hrs' : 3, 'description' : 'A historical survey of the evolution of jazz from primitive African elements through its fusion with Western hymns, work songs and military music. Various styles of jazz will be studied from Dixieland through modern/contemporary jazz forms.'},

    {'class_id' : 'MUT 1011', 'cname' : 'Music Fundamentals', 'fall': True, 'spring': True, 'summer': True, 'comp_sci' : False, 'data_sci' : False, 'info_sci' : False, 'info_tech' : False, 'info_sys' : False, 'communication': False, 'humanities' : True, 'social_sci': False, 'math_stats' : False, 'science' : False, 'completed' : False, 'credit_hrs' : 3, 'description' : 'The materials of Music: rhythm, melody, tempo, dynamics, harmony, texture, tonality, timbre, form, style, mood. Selected skills in music: listening, singing, reading, playing instruments.'},

    {'class_id' : 'MUT 1111', 'cname' : 'Theory I', 'fall': True, 'spring': True, 'summer': True, 'comp_sci' : False, 'data_sci' : False, 'info_sci' : False, 'info_tech' : False, 'info_sys' : False, 'communication': False, 'humanities' : True, 'social_sci': False, 'math_stats' : False, 'science' : False, 'completed' : False, 'credit_hrs' : 3, 'description' : 'Corequisite: MUT1241; The course consists of an introduction to the basics of music theory and the techniques and concepts of voice leading as practiced during the common practice period.'},

    {'class_id' : 'PHI 2100', 'cname' : '(GW) Art of Reasoning', 'fall': True, 'spring': True, 'summer': True, 'comp_sci' : False, 'data_sci' : False, 'info_sci' : False, 'info_tech' : False, 'info_sys' : False, 'communication': False, 'humanities' : True, 'social_sci': False, 'math_stats' : False, 'science' : False, 'completed' : False, 'credit_hrs' : 3, 'description' : 'This course is an introduction to the art of thinking and reasoning well. Thinking and reasoning well are of paramount importance for not only philosophy, science, history, politics, business, medicine, or engineering, but for any human endeavor that seeks to give rational support for its assertions. Throughout the course we will seek to refine the habits, patterns, and activities of thinking so as to become more careful, more critical, and more competent thinkers. We will do this by first cultivating the skills of identifying and evaluating arguments; we will then learn to identify patterns of bad reasoning and how to improve an argument. At various points in the course we will turn our critical thinking skills toward selected contemporary issues for analysis. By the time the course is finished, successful students will be more confident in analyzing the arguments of others, constructing their own arguments, and discoursing civily with others about complex and contentious issues.'},

    {'class_id' : 'PHI 2630', 'cname' : '(GW) Ethical Issues', 'fall': True, 'spring': True, 'summer': True, 'comp_sci' : False, 'data_sci' : False, 'info_sci' : False, 'info_tech' : False, 'info_sys' : False, 'communication': False, 'humanities' : True, 'social_sci': False, 'math_stats' : False, 'science' : False, 'completed' : False, 'credit_hrs' : 3, 'description' : 'This course is an introduction to thinking critically about a range of ethical issues. As such, we will examine the differences between opinions and positions, debates and arguments, and stereotypes and assumptions. We will learn to identify, analyze, and respond to arguments using ethical standards and logical criteria. Because ethical issues are often heated and emotionally charged, we will spend time focusing on how to listen to one another, building our community around intellectually safe inquiries. In order to engage these questions together, we will develop a basic theoretical framework from which to begin, and then drawing on significant philosophical theories of ethics, we will focus our attention on selected issues, which may include but are not limited to issues such as abortion, euthanasia, informed consent, research ethics, food justice, friendship, sex, cheating, and parenting'},

    {'class_id' : 'PUP 2312', 'cname' : 'Race, Gender & Politics', 'fall': True, 'spring': True, 'summer': True, 'comp_sci' : False, 'data_sci' : False, 'info_sci' : False, 'info_tech' : False, 'info_sys' : False, 'communication': False, 'humanities' : True, 'social_sci': False, 'math_stats' : False, 'science' : False, 'completed' : False, 'credit_hrs' : 3, 'description' : 'This course introduces students to the struggle of minorities and women to participate in the formation of public policy in the United States.'},

    {'class_id' : 'REL 2300', 'cname' : 'Comparative Religion', 'fall': True, 'spring': True, 'summer': True, 'comp_sci' : False, 'data_sci' : False, 'info_sci' : False, 'info_tech' : False, 'info_sys' : False, 'communication': False, 'humanities' : True, 'social_sci': False, 'math_stats' : False, 'science' : False, 'completed' : False, 'credit_hrs' : 3, 'description' : 'Comparative Religion first introduces students to the major religions of the world, and then seeks points of comparison between those religions in an effort to come to terms with the common bases of human religious experience.'},

    {'class_id' : 'REL 3102', 'cname' : 'Religion as Culture', 'fall': True, 'spring': True, 'summer': True, 'comp_sci' : False, 'data_sci' : False, 'info_sci' : False, 'info_tech' : False, 'info_sys' : False, 'communication': False, 'humanities' : True, 'social_sci': False, 'math_stats' : False, 'science' : False, 'completed' : False, 'credit_hrs' : 3, 'description' : 'This course will introduce students to one of the primary approaches to Religious Studies: the Social Scientific Study of religion as culture (other, complementary, approaches being History of Religions/Comparative Religions and Philosophy of Religion). We will begin with a unit examining classical theorists (Durkhiem and Weber), current theoretical developments and exploring some key methodological issues. In Units Two and Three we will draw on case studies illustrating religious diversity to refine/apply our understanding of theory and method.'},

    {'class_id' : 'SOP 3742', 'cname' : 'Psychology of Women', 'fall': True, 'spring': True, 'summer': True, 'comp_sci' : False, 'data_sci' : False, 'info_sci' : False, 'info_tech' : False, 'info_sys' : False, 'communication': False, 'humanities' : True, 'social_sci': False, 'math_stats' : False, 'science' : False, 'completed' : False, 'credit_hrs' : 3, 'description' : 'This course involves an investigation of the major theories as they relate to psychology of gender. Findings from the field of psychology regarding aspects of sexual differentiation and gender roles in general, and for women in particular, will be explored.'},

    {'class_id' : 'SYD 3700', 'cname' : 'Racial and Ethnic Minorities', 'fall': True, 'spring': True, 'summer': True, 'comp_sci' : False, 'data_sci' : False, 'info_sci' : False, 'info_tech' : False, 'info_sys' : False, 'communication': False, 'humanities' : True, 'social_sci': False, 'math_stats' : False, 'science' : False, 'completed' : False, 'credit_hrs' : 3, 'description' : 'This is an upper-level survey course that analyzes race and ethnicity through a sociological lens with attention to historical, political, and social contexts of racial issues. The course examines the formation and transformation of racial systems throughout US history, with a particular focus on colonialism, slavery, and segregation. Students will examine relevant sociological theories of race and ethnicity, including the social construction of race as well as the significance of structural racism across contemporary social institutions. The dynamics of race and ethnicity are also explored in relation to other social identities such as class, gender, and nationality.'},

    {'class_id' : 'SYD 3800', 'cname' : 'Gender and Society', 'fall': True, 'spring': True, 'summer': True, 'comp_sci' : False, 'data_sci' : False, 'info_sci' : False, 'info_tech' : False, 'info_sys' : False, 'communication': False, 'humanities' : True, 'social_sci': False, 'math_stats' : False, 'science' : False, 'completed' : False, 'credit_hrs' : 3, 'description' : 'This course is designed to explore the social meanings and political implications of gender in society. It will focus on gender as a taken-for-granted but problematic component of our lives, whether we are female or male. Sociologists now recognize that gender is a "social construction" which is open to re-definition and which has profound social implications. The course will explore topics such as: gender and sex role socialization; gender relationships; cross-cultural gender comparisons; and the effects of "the sex-gender system" on areas such as health, family life, religion, employment, crime, education, politics, and social change.'},

    {'class_id' : 'SYG 2013', 'cname' : 'Sex, Race and Class', 'fall': True, 'spring': True, 'summer': True, 'comp_sci' : False, 'data_sci' : False, 'info_sci' : False, 'info_tech' : False, 'info_sys' : False, 'communication': False, 'humanities' : True, 'social_sci': False, 'math_stats' : False, 'science' : False, 'completed' : False, 'credit_hrs' : 3, 'description' : 'This class is designed to introduce students to the Sociological study of the issues of Race, Sex, and Social Class. In this class, we will examine a number of issues facing American society today and how these issues are inter-related. Special emphasis will be placed on discussing how those problems are (or are not) dealt with in our society.'},

    {'class_id' : 'WOH 1012', 'cname' : '(GW) World History I', 'fall': True, 'spring': True, 'summer': True, 'comp_sci' : False, 'data_sci' : False, 'info_sci' : False, 'info_tech' : False, 'info_sys' : False, 'communication': False, 'humanities' : True, 'social_sci': False, 'math_stats' : False, 'science' : False, 'completed' : False, 'credit_hrs' : 3, 'description' : 'This course will provide a survey of world history from earliest human prehistory to the later middle ages. It will introduce students to the major civilizations and societies of Europe, Asia, Africa and the Americas. It will trace key developments in political organization, religion, culture and society in the different regions of the world, and will compare those developments in order to provide insight into the fundamental dynamics of human history. The course will also explore the interactions between the different regions, in order to assess the role of intercultural contacts in promoting change in human societies. Gordon Rule additional writing credit.'},

    {'class_id' : 'WOH 1022', 'cname' : '(GW) World History II', 'fall': True, 'spring': True, 'summer': True, 'comp_sci' : False, 'data_sci' : False, 'info_sci' : False, 'info_tech' : False, 'info_sys' : False, 'communication': False, 'humanities' : True, 'social_sci': False, 'math_stats' : False, 'science' : False, 'completed' : False, 'credit_hrs' : 3, 'description' : 'This course will provide a survey of world history from the later middle ages to the present. It will introduce students to the major civilizations and societies of Europe, Asia, Africa and the Americas. It will trace key developments in political organization, religion, culture and society in the different regions of the world, and will compare those developments in order to provide insight into the fundamental dynamics of human history. The course will also explore the interactions between the different regions, in order to assess the role of intercultural contacts in promoting change in human societies. Gordon Rule additional writing credit.'},

    #Reasoning and Analyzing Quantitatively and/or Understanding the Scientific Method (4-6 Hours) 
    {'class_id' : 'MGF 1113', 'cname' : 'Math for Teachers I', 'fall': True, 'spring': True, 'summer': True, 'comp_sci' : False, 'data_sci' : False, 'info_sci' : False, 'info_tech' : False, 'info_sys' : False, 'communication': False, 'humanities' : False, 'social_sci': False, 'math_stats' : True, 'science' : False, 'completed' : False, 'credit_hrs' : 3, 'description' : 'This course provides an introduction to Problem-Solving Processes, Strategies for Problem-Solving Sets and Numeration, Whole Numbers, Integers, Rational Numbers, Geometric Shapes, and Measurement and Geometry.'},

    {'class_id' : 'MAC 1101', 'cname' : 'Intensive College Algebra', 'fall': True, 'spring': True, 'summer': True, 'comp_sci' : False, 'data_sci' : False, 'info_sci' : False, 'info_tech' : False, 'info_sys' : False, 'communication': False, 'humanities' : False, 'social_sci': False, 'math_stats' : True, 'science' : False, 'completed' : False, 'credit_hrs' : 3, 'description' : 'Prerequisite:  Permission of the Department; This course is designed for the student who has some knowledge of Intermediate Algebra, but who is not ready for College Algebra (MAC 1105). This course reviews key topics in Intermediate Algebra and it covers the material in College Algebra, linear functions, quadratic functions, inequalities, polynomials, exponentials, and logarithms. Students may not receive credit for this course and MAC 1105 (College Algebra) or MAC 1147 (Precalculus).'},

    {'class_id' : 'MAC 1101C', 'cname' : 'Intensive College Algebra with Recitation', 'fall': True, 'spring': True, 'summer': True, 'comp_sci' : False, 'data_sci' : False, 'info_sci' : False, 'info_tech' : False, 'info_sys' : False, 'communication': False, 'humanities' : False, 'social_sci': False, 'math_stats' : True, 'science' : False, 'completed' : False, 'credit_hrs' : 3, 'description' : 'Prerequisite:  Qualifying score on math placement OR C or better in MAT1033 or equivalent; Topics include a substantial review of Intermediate Algebra concepts, linear and quadratic functions, systems of equations and inequalities, polynomials, exponentials, logarithms, and applications. Students attend four hours of lecture and one hour of recitation per week. Students may only earn credit for one of the following: MAC1105, MAC1105C, or MAC1101C. Meets the General Education requirement in Mathematics. Meets the Gordon Rule requirement.'},

    {'class_id' : 'MAC 1105C', 'cname' : 'College Algebra with Recitation', 'fall': True, 'spring': True, 'summer': True, 'comp_sci' : False, 'data_sci' : False, 'info_sci' : False, 'info_tech' : False, 'info_sys' : False, 'communication': False, 'humanities' : False, 'social_sci': False, 'math_stats' : True, 'science' : False, 'completed' : False, 'credit_hrs' : 3, 'description' : 'Prerequisite:  Qualifying score on math placement or equivalent; Topics include a review of Intermediate Algebra concepts, linear and quadratic functions, systems of equations and inequalities, polynomials, exponentials, logarithms, and applications. Students attend three hours of lecture and one hour of recitation per week. Students may only earn credit for one of the following: MAC1105, MAC1105C, or MAC1101C. Meets the General Education requirement in Mathematics. Meets the Gordon Rule requirement.'},

    {'class_id' : 'AST 2002L', 'cname' : 'Discovering Astronomy Lab', 'fall': True, 'spring': True, 'summer': True, 'comp_sci' : False, 'data_sci' : False, 'info_sci' : False, 'info_tech' : False, 'info_sys' : False, 'communication': False, 'humanities' : False, 'social_sci': False, 'math_stats' : False, 'science' : True, 'completed' : False, 'credit_hrs' : 1, 'description' : 'This is an introductory laboratory course focused on student-driven experiments and scientific thinking. Students will explore astronomical phenomena and test scientific relationships on topics including the sun, moon, planets, stars, galaxies, and telescopes. This course will include three hours of laboratory. Availability: This course is normally available Summer, Fall and Spring terms. Course Fees: $25'},

    {'class_id' : 'BSC 1930', 'cname' : 'Current Applications in Biology', 'fall': True, 'spring': True, 'summer': True, 'comp_sci' : False, 'data_sci' : False, 'info_sci' : False, 'info_tech' : False, 'info_sys' : False, 'communication': False, 'humanities' : False, 'social_sci': False, 'math_stats' : False, 'science' : True, 'completed' : False, 'credit_hrs' : 2, 'description' : 'In this course biological principles and research are applied to modern life. Topics will vary from semester to semester.'},

    {'class_id' : 'CHM 1025', 'cname' : 'Introduction to Chemistry', 'fall': True, 'spring': True, 'summer': True, 'comp_sci' : False, 'data_sci' : False, 'info_sci' : False, 'info_tech' : False, 'info_sys' : False, 'communication': False, 'humanities' : False, 'social_sci': False, 'math_stats' : False, 'science' : True, 'completed' : False, 'credit_hrs' : 2, 'description' : 'This course is an introduction to the principles of modern chemistry and an overview of different areas of chemistry and its applications including elementary organic chemistry.'},

    {'class_id' : 'CHM 1025L', 'cname' : 'Introduction to Chemistry Lab', 'fall': True, 'spring': True, 'summer': True, 'comp_sci' : False, 'data_sci' : False, 'info_sci' : False, 'info_tech' : False, 'info_sys' : False, 'communication': False, 'humanities' : False, 'social_sci': False, 'math_stats' : False, 'science' : True, 'completed' : False, 'credit_hrs' : 1, 'description' : 'Co-requisite: CHM 1025; This course is an introduction to the principles of modern chemistry and an overview of different areas of chemistry and its applications including elementary organic chemistry. (A laboratory fee of $59 will be assessed.)'},

    {'class_id' : 'CHM 2045L', 'cname' : 'General Chemistry I Laboratory', 'fall': True, 'spring': True, 'summer': True, 'comp_sci' : False, 'data_sci' : False, 'info_sci' : False, 'info_tech' : False, 'info_sys' : False, 'communication': False, 'humanities' : False, 'social_sci': False, 'math_stats' : False, 'science' : True, 'completed' : False, 'credit_hrs' : 1, 'description' : 'Prerequisite:  CHM 1025, CHM 1025L or high school chemistry with a B or better, MAC 1105; Co-requisite: CHM 2045; The course includes experiments that demonstrate the concepts of stoichiometry, atomic structure, chemical bonding, acids and bases, solutions and their properties, reaction rates and equilibrium and descriptive chemistry of selected elements. (A laboratory fee of $59 will be assessed.)'},

    {'class_id' : 'HUN 1001', 'cname' : 'Introduction to Nutrition Science', 'fall': True, 'spring': True, 'summer': True, 'comp_sci' : False, 'data_sci' : False, 'info_sci' : False, 'info_tech' : False, 'info_sys' : False, 'communication': False, 'humanities' : False, 'social_sci': False, 'math_stats' : False, 'science' : True, 'completed' : False, 'credit_hrs' : 2, 'description' : 'Prerequisite:  BSC 1005C; This course is an introduction to nutrition science using the scientific method and natural sciences principles from biology and chemistry to explore nutrient structures, usage/metabolism, functions, sources, standards, and roles in health and disease; and basic research methods.'},

    {'class_id' : 'HUN 2201', 'cname' : 'Basic Principles of Human Nutrition', 'fall': True, 'spring': True, 'summer': True, 'comp_sci' : False, 'data_sci' : False, 'info_sci' : False, 'info_tech' : False, 'info_sys' : False, 'communication': False, 'humanities' : False, 'social_sci': False, 'math_stats' : False, 'science' : True, 'completed' : False, 'credit_hrs' : 3, 'description' : 'HUN 2201, Basic Principles of Nutrition, is an introductory course in food and nutrition science relative to the health and well-being of the individual and the community. The functions and chemical composition of the essential nutrients, and how they are processed and utilized in the body are discussed. Dietary habits, nutrient requirements, food choices, healthy eating practices, menu planning, shopping for food and food preparation are studied. Myths and misinformation about nutrition are identified and evaluated based on the scientific evidence. This course meets the 3 credits non-lab course requirement toward the General Education Natural Science requirements and learning through reflective judgment.'},

    {'class_id' : 'IDC 2000', 'cname' : 'The Beauty and Joy of Computing', 'fall': True, 'spring': True, 'summer': True, 'comp_sci' : False, 'data_sci' : False, 'info_sci' : False, 'info_tech' : False, 'info_sys' : False, 'communication': False, 'humanities' : False, 'social_sci': False, 'math_stats' : False, 'science' : True, 'completed' : False, 'credit_hrs' : 3, 'description' : 'The course focuses on teaching students some of the Big Ideas of Computing such as abstraction, design, recursion, concurrency, simulations, and the limits of computation. The course also provides a historic perspective of Computing and where it is heading. Throughout the course, we will emphasis the relevance of Computing to the students, their future studies, their careers, and society. In this course students will learn Python as the programming language to deliver the concepts. Given that data is pervasive and the need to analyze data is in almost every discipline, learning Python that early will enable students to conduct data analysis which will be helpful for their studies at UNF and in their careers.'},

    {'class_id' : 'PHI 2101', 'cname' : 'Introduction to Logic', 'fall': True, 'spring': True, 'summer': True, 'comp_sci' : False, 'data_sci' : False, 'info_sci' : False, 'info_tech' : False, 'info_sys' : False, 'communication': False, 'humanities' : False, 'social_sci': False, 'math_stats' : False, 'science' : True, 'completed' : False, 'credit_hrs' : 3, 'description' : 'This course will introduce students to symbolic logic. In logic we study the principles of correct reasoning as revealed through language. In this course, students will study both how and why good reasoning works. Our focus will be on the principles of deductive reasoning (in contrast to inductive reasoning). In symbolic logic we use artificial, formal languages to study deductive inferences. In this course students will be introduced to and come to understand two such formal languages (sentential logic and predicate logic) in order to assess and construct good deductive arguments and test for other logical properties. This course satisfies a core requirement for the major in Philosophy.'},

    {'class_id' : 'PHY 1020L', 'cname' : 'Discovering Physics Laboratory: How things work', 'fall': True, 'spring': True, 'summer': True, 'comp_sci' : False, 'data_sci' : False, 'info_sci' : False, 'info_tech' : False, 'info_sys' : False, 'communication': False, 'humanities' : False, 'social_sci': False, 'math_stats' : False, 'science' : True, 'completed' : False, 'credit_hrs' : 1, 'description' : 'Co-requisite: PHY 1020; This laboratory will explore fundamental concepts in physics and how these concepts can be used to understand the world around us. It is to be taken with PHY1020 as a co-requisite. Topics covered include force, energy, electricity, magnetism, and the structure of matter. The laboratory will emphasize conceptual understanding rather than mathematical problem solving. This laboratory is not intended for students planning to major in science or engineering. Course Fees: $25'},

    {'class_id' : 'PHY 1028', 'cname' : 'Introduction to Physics', 'fall': True, 'spring': True, 'summer': True, 'comp_sci' : False, 'data_sci' : False, 'info_sci' : False, 'info_tech' : False, 'info_sys' : False, 'communication': False, 'humanities' : False, 'social_sci': False, 'math_stats' : False, 'science' : True, 'completed' : False, 'credit_hrs' : 2, 'description' : 'The lecture is to prepare STEM majors for the lower-level physics course sequences in both calculus-based and algebra-based physics. This course is an introduction to classical physics involving a study of motion, fundamental forces, conservation laws of energy and momentum, light waves, electricity and magnetism. An exposure to the philosophy of science and the scientific method forms an essential component of this course. This course cannot be used by natural sciences majors to satisfy degree requirements.'},

    {'class_id' : 'PHY 1028L', 'cname' : 'Introduction to Physics Lab', 'fall': True, 'spring': True, 'summer': True, 'comp_sci' : False, 'data_sci' : False, 'info_sci' : False, 'info_tech' : False, 'info_sys' : False, 'communication': False, 'humanities' : False, 'social_sci': False, 'math_stats' : False, 'science' : True, 'completed' : False, 'credit_hrs' : 1, 'description' : 'Co-requisite: PHY1028; This course explores the topics covered in the lecture course in a laboratory setting. This course focuses on student-driven experimental design and scientific thinking. This course is designed to allow students to explore physical phenomena and test relationships in part by self-inquiry. The skills acquired in this course can be applied in scientific and non-scientific industries. The laboratory exercises will involve topics such as kinematics of free fall and projectile motion, forces, laws of conservation of energy, optical laws of reflection and refraction, the behavior of lenses, and wave phenomena.'},

    {'class_id' : 'PHY 2464C', 'cname' : 'The Physics of Music', 'fall': True, 'spring': True, 'summer': True, 'comp_sci' : False, 'data_sci' : False, 'info_sci' : False, 'info_tech' : False, 'info_sys' : False, 'communication': False, 'humanities' : False, 'social_sci': False, 'math_stats' : False, 'science' : True, 'completed' : False, 'credit_hrs' : 3, 'description' : 'Prerequisites:MAC1105 or MAC1101 or MAC1101C or MAC1105C AND MAC1114 or MAC1147; This is a science course, that includes an integrated laboratory, designed for music majors. The course will cover the fundamental principles governing the physics of sounds, musical instruments, the human voice, the acoustics of rooms, electroacoustics, and electronic music technology. The lab component of the course will allow students to explore the subjects presented in the lecture through hands-on experiments. The course will often employ some elementary mathematics, including algebra and some simple trigonometry.'},

    {'class_id' : 'PHY 2053L', 'cname' : 'Algebra-Based Physics I Lab', 'fall': True, 'spring': True, 'summer': True, 'comp_sci' : False, 'data_sci' : False, 'info_sci' : False, 'info_tech' : False, 'info_sys' : False, 'communication': False, 'humanities' : False, 'social_sci': False, 'math_stats' : False, 'science' : True, 'completed' : False, 'credit_hrs' : 1, 'description' : 'Co-requisite: PHY 2053; This course is the laboratory course that accompanies PHY 2053. This course will be three hours of laboratory. Course Fees: $25'},

    {'class_id' : 'PHY 2054', 'cname' : 'Algebra-Based Physics II', 'fall': True, 'spring': True, 'summer': True, 'comp_sci' : False, 'data_sci' : False, 'info_sci' : False, 'info_tech' : False, 'info_sys' : False, 'communication': False, 'humanities' : False, 'social_sci': False, 'math_stats' : False, 'science' : True, 'completed' : False, 'credit_hrs' : 3, 'description' : 'Prerequisite:  PHY 2053; This course is an introduction to electricity, magnetism, light and modern physics. Calculus is not required in this course. This course will be three hours of lecture.'},

    {'class_id' : 'PHY 2054L', 'cname' : 'Algebra-Based Physics II Lab', 'fall': True, 'spring': True, 'summer': True, 'comp_sci' : False, 'data_sci' : False, 'info_sci' : False, 'info_tech' : False, 'info_sys' : False, 'communication': False, 'humanities' : False, 'social_sci': False, 'math_stats' : False, 'science' : True, 'completed' : False, 'credit_hrs' : 1, 'description' : 'Co-requisite: PHY 2054; This course is the laboratory course that accompanies PHY 2054. This course will be three hours of laboratory. Course Fees: $25'},


]

prereq_details = [
    #Compuer Science specific prerequisites, read as "Course (course_id) has the prequisite (prerequisite_id) 
    {'course_id': 'CIS 3253', 'prerequisite_id': 'COP 2220'},
    {'course_id': 'COP 3503', 'prerequisite_id': 'COP 2220'},
    {'course_id': 'CDA 3100', 'prerequisite_id': 'COP 2220'},
    {'course_id': 'COT 3210', 'prerequisite_id': 'COT 3100'},
    {'course_id': 'COP 3530', 'prerequisite_id': 'COT 3100'},
    {'course_id': 'COP 3530', 'prerequisite_id': 'COP 3503'},
    {'course_id': 'CNT 4504', 'prerequisite_id': 'COP 3503'},
    {'course_id': 'COP 3703', 'prerequisite_id': 'COP 3503'},
    {'course_id': 'COP 3404', 'prerequisite_id': 'COP 3503'},
    {'course_id': 'COP 3404', 'prerequisite_id': 'CDA 3100'},
    {'course_id': 'COP 4620', 'prerequisite_id': 'COT 3210'},
    {'course_id': 'COP 4620', 'prerequisite_id': 'COP 3530'},
    {'course_id': 'CEN 4010', 'prerequisite_id': 'COP 3530'},
    {'course_id': 'COT 4400', 'prerequisite_id': 'COP 3530'},
    {'course_id': 'CAP 4630', 'prerequisite_id': 'COP 3530'},
    {'course_id': 'COP 4610', 'prerequisite_id': 'COP 3530'},
    {'course_id': 'COP 4610', 'prerequisite_id': 'COP 3404'},
    {'course_id': 'CEN 4010', 'prerequisite_id': 'COP 3703'},
    {'course_id': 'CAP 3784', 'prerequisite_id': 'COP 3530'},
    {'course_id': 'MAC 2312', 'prerequisite_id': 'MAC 2311'},
    {'course_id': 'PHY 2048C', 'prerequisite_id': 'MAC 2311'},
    {'course_id': 'MAS 3105', 'prerequisite_id': 'MAC 2312'},
    {'course_id': 'STA 4321', 'prerequisite_id': 'MAC 2312'},
    {'course_id': 'MAS 3032', 'prerequisite_id': 'MAC 2312'},
    {'course_id': 'STA 3164', 'prerequisite_id': 'STA 3163'},
    {'course_id': 'PHY 2048C', 'prerequisite_id': 'PHY 2049'},
    {'course_id': 'COT 4560', 'prerequisite_id': 'COP 3530'},
    {'course_id': 'STA 4504', 'prerequisite_id': 'STA 3163'},
    {'course_id': 'ENC 2210', 'prerequisite_id': 'ENC 1101'},
    {'course_id': 'CAP 4770', 'prerequisite_id': 'COP 3703'},
    {'course_id': 'CAP 4764', 'prerequisite_id': 'COP 3703'},
    {'course_id': 'CIS 3526', 'prerequisite_id': 'COP 2220'},
    {'course_id': 'COP 4640', 'prerequisite_id': 'COP 3503'},
    {'course_id': 'CIS 4360', 'prerequisite_id': 'COP 3503'},
    {'course_id': 'CIS 4325', 'prerequisite_id': 'CNT 4504'},
    {'course_id': 'CIS 4325', 'prerequisite_id': 'COP 4640'},
    {'course_id': 'CNT 4406', 'prerequisite_id': 'CNT 4504'},
    {'course_id': 'CEN 4083', 'prerequisite_id': 'CNT 4504'},
    {'course_id': 'CIS 4364', 'prerequisite_id': 'CNT 4504'},
    {'course_id': 'CIS 4366', 'prerequisite_id': 'CIS 4360'},
    {'course_id': 'CIS 4364', 'prerequisite_id': 'CIS 4360'},
    {'course_id': 'COP 3855', 'prerequisite_id': 'COP 2220'},
    {'course_id': 'COP 4813', 'prerequisite_id': 'COP 3503'},
    {'course_id': 'CDA 4010', 'prerequisite_id': 'COP 3503'},
    {'course_id': 'CIS 4327', 'prerequisite_id': 'COP 3855'},
    {'course_id': 'CIS 4327', 'prerequisite_id': 'COP 3530'},
    {'course_id': 'CIS 4327', 'prerequisite_id': 'COP 3703'},
    {'course_id': 'CAP 3784', 'prerequisite_id': 'COP 3703'},
    {'course_id': 'CIS 4328', 'prerequisite_id': 'COP 4813'},
    {'course_id': 'CIS 4328', 'prerequisite_id': 'CIS 4327'},

    ]

try:
    # Execute bulk insert
    session.execute(insert(Course).values(course_details))
    session.commit()
    print("Bulk insertion successful.")
except IntegrityError as e:
    session.rollback()  # Roll back changes to avoid partial insertions
    print(f"IntegrityError: {e}")
    print("Skipped duplicate entries.")

for p in prereq_details:
    try:
        p = association_table.insert().values(**p)
        session.execute(p)
        session.commit()
    except IntegrityError:
        session.rollback()



session.commit()


courses = session.query(Course).all()

'''for course in courses:
    print(course.cname, course.completed)
    prerequisites = course.prerequisites
    if prerequisites:
        print("Prerequisites:")
        for prereq in prerequisites:
            print(f"- {prereq.class_id}")
    else:
        print("No Prerequisites")
    print()'''


#classes = session.query(Course).filter( (Course.comp_sci == True) & (Course.data_sci == True)).all()
#Check for completed classes and track credit hours of each group i.e., communication, humanities, etc.
#check completed for each category, count total comleted hours, add more classes until it reaches the appropriate number
#communication = 9, humanities = 9, social sciences = 6, math/stats = 3, science = 3, math/stats AND/OR science = 6, total >= 36

total_hrs = 0
comm_hrs = 0
humanities_hrs = 0
social_hrs = 0
math_stat_hrs = 0
science_hrs = 0
to_schedule = []

#--------------if computer science major
major_compsci = session.query(Course).filter(Course.comp_sci == True).filter(Course.completed == False)
for m in major_compsci:
    to_schedule.append(m)
    if (m.communication == True):
        comm_hrs += m.credit_hrs
    if (m.humanities == True):
        humanities_hrs += m.credit_hrs
    if (m.social_sci == True):
        social_hrs += m.credit_hrs
    if (m.math_stats == True):
        math_stat_hrs += m.credit_hrs
    if (m.science == True):
        science_hrs += m.credit_hrs
    total_hrs += m.credit_hrs

#---------------if data science major
'''major_datasci = session.query(Course).filter(Course.data_sci == True).filter(Course.completed == False)
for m in major_datasci:
    to_schedule.append(m)
    if (m.communication == True):
        comm_hrs += m.credit_hrs
    if (m.humanities == True):
        humanities_hrs += m.credit_hrs
    if (m.social_sci == True):
        social_hrs += m.credit_hrs
    if (m.math_stats == True):
        math_stat_hrs += m.credit_hrs
    if (m.science == True):
        science_hrs += m.credit_hrs
    total_hrs += m.credit_hrs'''

#--------------if information science major
'''major_infosci = session.query(Course).filter(Course.info_sci == True).filter(Course.completed == False)
for m in major_infosci:
    to_schedule.append(m)
    if (m.communication == True):
        comm_hrs += m.credit_hrs
    if (m.humanities == True):
        humanities_hrs += m.credit_hrs
    if (m.social_sci == True):
        social_hrs += m.credit_hrs
    if (m.math_stats == True):
        math_stat_hrs += m.credit_hrs
    if (m.science == True):
        science_hrs += m.credit_hrs
    total_hrs += m.credit_hrs'''

#-------------if information systems major
'''major_infosys = session.query(Course).filter(Course.info_sys == True).filter(Course.completed == False)
for m in major_infosys:
    to_schedule.append(m)
    if (m.communication == True):
        comm_hrs += m.credit_hrs
    if (m.humanities == True):
        humanities_hrs += m.credit_hrs
    if (m.social_sci == True):
        social_hrs += m.credit_hrs
    if (m.math_stats == True):
        math_stat_hrs += m.credit_hrs
    if (m.science == True):
        science_hrs += m.credit_hrs
    total_hrs += m.credit_hrs'''

#------------if information technology major
'''major_infotech = session.query(Course).filter(Course.info_tech == True).filter(Course.completed == False)
for m in major_infotech:
    to_schedule.append(m)
    if (m.communication == True):
        comm_hrs += m.credit_hrs
    if (m.humanities == True):
        humanities_hrs += m.credit_hrs
    if (m.social_sci == True):
        social_hrs += m.credit_hrs
    if (m.math_stats == True):
        math_stat_hrs += m.credit_hrs
    if (m.science == True):
        science_hrs += m.credit_hrs
    total_hrs += m.credit_hrs'''

done = session.query(Course).filter(Course.completed == True).all()

# ---------------------------------------------------General Education 
for d in done:
    if (d.communication == True):
        comm_hrs += d.credit_hrs
    if (d.humanities == True):
        humanities_hrs += d.credit_hrs
    if (d.social_sci == True):
        social_hrs += d.credit_hrs
    if (d.math_stats == True):
        math_stat_hrs += d.credit_hrs
    if (d.science == True):
        science_hrs += d.credit_hrs
    
scheduled_class_ids = [course.class_id for course in to_schedule]

#querying !completed removes possible duplicates

#----------------communications needed
must_take = session.query(Course).filter( Course.class_id == 'ENC 1101' ).first()
if (must_take.completed == False):
    to_schedule.append(must_take)
    comm_hrs += int(must_take.credit_hrs) 
all_comm_classes = session.query(Course).filter(Course.communication == True).filter(Course.completed == False).filter(Course.class_id != 'ENC 1101').filter(~Course.class_id.in_(scheduled_class_ids)).all()
while comm_hrs < 9:
    #random.sample() is remvoing the result from the list so no duplicates will be produced
    comm_picked = random.sample(all_comm_classes, 1)
    to_schedule.append(comm_picked[0])
    comm_hrs += int(comm_picked[0].credit_hrs)

#----------------humanities needed
all_hum_classes = session.query(Course).filter(Course.humanities == True).filter(Course.completed == False).filter(~Course.class_id.in_(scheduled_class_ids)).all()
while humanities_hrs < 9:
    hum_picked = random.sample(all_hum_classes, 1)
    to_schedule.append(hum_picked[0])
    humanities_hrs += int(hum_picked[0].credit_hrs)

#----------------social sciences needed 
all_social_classes = session.query(Course).filter(Course.social_sci == True).filter(Course.completed == False).filter(~Course.class_id.in_(scheduled_class_ids)).all()
while social_hrs < 6:
    social_picked = random.sample(all_social_classes, 1)
    to_schedule.append(social_picked[0])
    social_hrs += int(social_picked[0].credit_hrs)

all_mathstat_classes = session.query(Course).filter(Course.math_stats == True).filter(Course.completed == False).filter(~Course.class_id.in_(scheduled_class_ids)).all()
if math_stat_hrs < 3:
    mathstat_picked = random.sample(all_mathstat_classes, 1)
    to_schedule.append(mathstat_picked[0])
    math_stat_hrs += int(mathstat_picked[0].credit_hrs)
    
all_science_classes = session.query(Course).filter(Course.science == True).filter(Course.completed == False).filter(~Course.class_id.in_(scheduled_class_ids)).all()
if science_hrs < 3:
    science_picked = random.sample(all_science_classes, 1)
    to_schedule.append(science_picked[0])
    science_hrs += int(science_picked[0].credit_hrs)

all_either_classes = session.query(Course).filter( (Course.science == True) | (Course.math_stats == True) ).filter(Course.completed == False).filter(~Course.class_id.in_(scheduled_class_ids)).all()
while (math_stat_hrs + science_hrs) < 12:
    chosen = random.sample(all_either_classes, 1)
    if (chosen[0].math_stats == True):
        math_stat_hrs += int(chosen[0].credit_hrs)
    else:
        science_hrs += int(chosen[0].credit_hrs)

total_hrs += (comm_hrs + humanities_hrs + social_hrs + math_stat_hrs + science_hrs)

for cla in to_schedule:
    print(cla.class_id, cla.cname)

print("Total: ", total_hrs)

print()
