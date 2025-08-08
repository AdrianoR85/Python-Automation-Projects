"""
Global application settings
"""

# Window Setting
WINDOW_CONFIG = {
  'width': 930,
  'height': 478,
  'title': 'Employee Management System - Login',
  'resizable': False
}

# Visualizations Settings
COLORS = {
    'primary': '#2B2B2B',
    'secondary': '#FFFFFF', 
    'accent': '#1f538d',
    'text_primary': 'dark blue',
    'text_secondary': '#666666',
    'error': '#d32f2f',
    'success': '#388e3c'
}

# Font Settings
FONTS = {
    'title': ('Goudy Old Style', 20, 'bold'),
    'subtitle': ('Arial', 14, 'normal'),
    'button': ('Arial', 12, 'bold'),
    'entry': ('Arial', 11, 'normal')
}

#Asset paths
ASSETS = {
  'cover_image': 'assets/cover.png'
}

# Temporary credentials (will be removed when the backend is implemented)
TEMP_CREDENTIALS = {
    'username': 'admin',
    'password': 'admin123'
}