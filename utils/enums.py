from enum import Enum

class Priority(Enum):
    LOW = 'Low'
    MEDIUM = 'Medium'
    HIGH = 'High'

class FinancialHealth(Enum):
    V_POOR = 'very poor'
    POOR = 'Poor'
    FAIR = 'Fair'
    GOOD = 'Good'

class Rating(Enum):
    LOW = 'Low'
    MEDIUM = 'Medium'
    HIGH = 'High'

class ProjectStatus(Enum):
    STARTED = 'started'
    ENDED = 'ended'
    IN_PROGRESS = 'in progress'
    TERMINATED = 'terminated'
    COMPLETED = 'completed'
