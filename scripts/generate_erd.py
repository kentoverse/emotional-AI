from sqlalchemy import create_engine, Column, Integer, String, Enum, ForeignKey, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'Users'
    UserID = Column(Integer, primary_key=True, autoincrement=True)
    Name = Column(String(100), nullable=False)
    Email = Column(String(100), nullable=False, unique=True)
    Password = Column(String(255), nullable=False)
    ProfilePicture = Column(String(255))
    UserType = Column(Enum('Owner', 'Walker'), nullable=False)

class Interaction(Base):
    __tablename__ = 'Interactions'
    InteractionID = Column(Integer, primary_key=True, autoincrement=True)
    UserID = Column(Integer, ForeignKey('Users.UserID'))
    InteractionType = Column(Enum('Act', 'React', 'Attract'), nullable=False)
    InteractionContent = Column(Text, nullable=False)
    Timestamp = Column(DateTime, nullable=False)
    user = relationship("User", back_populates="interactions")

class Effect(Base):
    __tablename__ = 'Effects'
    EffectID = Column(Integer, primary_key=True, autoincrement=True)
    InteractionID = Column(Integer, ForeignKey('Interactions.InteractionID'))
    EffectType = Column(Enum('Negative', 'Positive', 'Neutral'), nullable=False)
    EffectDescription = Column(Text, nullable=False)
    ImpactLevel = Column(Integer, nullable=False)
    interaction = relationship("Interaction", back_populates="effects")

class Moment(Base):
    __tablename__ = 'Moments'
    MomentID = Column(Integer, primary_key=True, autoincrement=True)
    UserID = Column(Integer, ForeignKey('Users.UserID'))
    MomentType = Column(Enum('Past Reflection', 'Future Insight', 'Present Awareness'), nullable=False)
    Description = Column(Text, nullable=False)
    Timestamp = Column(DateTime, nullable=False)
    user = relationship("User", back_populates="moments")

class Relationship(Base):
    __tablename__ = 'Relationships'
    RelationshipID = Column(Integer, primary_key=True, autoincrement=True)
    UserID1 = Column(Integer, ForeignKey('Users.UserID'))
    UserID2 = Column(Integer, ForeignKey('Users.UserID'))
    RelationshipStatus = Column(String(50), nullable=False)
    StartDate = Column(DateTime, nullable=False)
    user1 = relationship("User", foreign_keys=[UserID1])
    user2 = relationship("User", foreign_keys=[UserID2])

User.interactions = relationship("Interaction", order_by=Interaction.InteractionID, back_populates="user")
User.moments = relationship("Moment", order_by=Moment.MomentID, back_populates="user")
Interaction.effects = relationship("Effect", order_by=Effect.EffectID, back_populates="interaction")

# Creating the SQLite engine with the path to your database file
engine = create_engine('sqlite:////Users/mocavada/code/emotional-AI/data/database.db')
Base.metadata.create_all(engine)

# Generating the ER diagram
render_er(Base, '../docs/erd/ERD_diagram.png')  # Saving the ERD in the docs/erd directory