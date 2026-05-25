import datetime
from sqlalchemy import Column, Integer, String, Text, Boolean, DateTime, ForeignKey
from shared.db import Base

class Profile(Base):
    __tablename__ = "profile"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, index=True, nullable=False)
    phone = Column(String(50), nullable=True)
    
    # Geographic Monitoring Fields
    preferred_indian_locations = Column(Text, default="Bangalore, Hyderabad")
    allow_foreign_remote = Column(Boolean, default=True)
    requires_visa_for_foreign_onsite = Column(Boolean, default=True)
    
    # Socials & Links
    linkedin_url = Column(Text, nullable=True)
    github_url = Column(Text, nullable=True)
    leetcode_url = Column(Text, nullable=True)
    
    # Academic & Professional Metrics
    university = Column(String(255), nullable=True)
    degree = Column(String(255), nullable=True)
    graduation_year = Column(Integer, nullable=True)
    cgpa = Column(String(10), nullable=True)
    notice_period = Column(String(100), nullable=True)
    salary_expectation_inr = Column(String(100), nullable=True)
    salary_expectation_usd = Column(String(100), nullable=True)
    work_authorization = Column(String(255), nullable=True)
    summary = Column(Text, nullable=True) # Holds master resume bullets & NLP project text
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

class Resume(Base):
    __tablename__ = "resume"
    
    id = Column(Integer, primary_key=True, index=True)
    type = Column(String(50), default="base") # "base" or "tailored"
    job_id = Column(Integer, ForeignKey("jobs.id"), nullable=True)
    content_text = Column(Text, nullable=False)
    pdf_path = Column(Text, nullable=True)
    latex_source = Column(Text, nullable=True)
    template_name = Column(String(100), default="jakes_resume")
    diff_json = Column(Text, nullable=True) # Used by React to show side-by-side changes
    match_score = Column(Integer, nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

class Job(Base):
    __tablename__ = "jobs"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    company = Column(String(255), nullable=False)
    location = Column(String(255), nullable=True)
    remote = Column(Boolean, default=False)
    source = Column(String(100), nullable=True) # LinkedIn, Indeed, etc.
    apply_link = Column(Text, nullable=True)
    full_jd = Column(Text, nullable=True)
    jd_snippet = Column(Text, nullable=True)
    ats_type = Column(String(100), nullable=True)
    status = Column(String(50), default="scraped") # scraped, tailored, applied, skipped
    resume_id = Column(Integer, nullable=True)
    applied_at = Column(DateTime, nullable=True)
    confirmation_screenshot = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

class Application(Base):
    __tablename__ = "applications"
    
    id = Column(Integer, primary_key=True, index=True)
    job_id = Column(Integer, ForeignKey("jobs.id"), nullable=False)
    status = Column(String(50), default="pending") # pending, auto_applied, manual_needed, done
    method = Column(String(50), default="browser_use")
    captcha_hit = Column(Boolean, default=False)
    confirmation_screenshot = Column(Text, nullable=True)
    notes = Column(Text, nullable=True)
    applied_at = Column(DateTime, nullable=True)

class OutreachContact(Base):
    __tablename__ = "outreach_contacts"
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), nullable=False)
    name = Column(String(255), nullable=True)
    company = Column(String(255), nullable=True)
    role = Column(String(255), nullable=True)
    linkedin_url = Column(Text, nullable=True)
    research_notes = Column(Text, nullable=True)
    status = Column(String(50), default="researched") # researched, drafted, approved, sent
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

class OutreachEmail(Base):
    __tablename__ = "outreach_emails"
    
    id = Column(Integer, primary_key=True, index=True)
    contact_id = Column(Integer, ForeignKey("outreach_contacts.id"), nullable=False)
    subject = Column(String(255), nullable=False)
    body = Column(Text, nullable=False)
    status = Column(String(50), default="draft") # draft, approved, sent, rejected
    gemini_research = Column(Text, nullable=True)
    sent_at = Column(DateTime, nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

class AgentRun(Base):
    __tablename__ = "agent_runs"
    
    id = Column(Integer, primary_key=True, index=True)
    triggered_by = Column(String(50), default="scheduler") # scheduler or manual
    started_at = Column(DateTime, default=datetime.datetime.utcnow)
    finished_at = Column(DateTime, nullable=True)
    jobs_found = Column(Integer, default=0)
    jobs_tailored = Column(Integer, default=0)
    applications_submitted = Column(Integer, default=0)
    emails_drafted = Column(Integer, default=0)
    emails_sent = Column(Integer, default=0)
    errors_json = Column(Text, nullable=True)
    status = Column(String(50), default="completed") # completed, partial, failed

class PortalSession(Base):
    __tablename__ = "portal_sessions"
    
    id = Column(Integer, primary_key=True, index=True)
    portal = Column(String(100), nullable=False) # indeed, naukri, glassdoor
    cookies_json = Column(Text, nullable=False)
    last_verified = Column(DateTime, default=datetime.datetime.utcnow)
    status = Column(String(50), default="active")