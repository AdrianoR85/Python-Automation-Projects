"""
Global application settings
"""

# Window settings
LOGIN_WINDOW_CONFIG = {
    'width': 930,  
    'height': 478,  
    'title': 'Employee Management System',
    'resizable': False
}

WINDOW_EMS = {
    'width': 986,  
    'height': 580,  
    'title': 'Employee Management System',
    'resizable': False, 
    'banner_height': 158
}

COLORS = {
    # Main colors
    'primary': '#3B82F6',       # Modern blue
    'primary_hover': '#2563EB', # Hover blue
    'secondary': '#F8FAFC',     # Very light gray
    'accent': '#10B981',        # Green for success
    
    # Text colors
    'text_primary': '#161C30',   # Dark blue
    'text_secondary': '#64748B', # Medium gray
    'text_light': '#FFFFFF',     # White
    
    # Background colors

    'bg_primary': '#FFFFFF',     # White
    'bg_secondary': '#161C30',   # Dark blue

    
    # Border colors
    'border_light': "#BABCBE",   # Light border
    'border_focus': '#3B82F6',   # Focus border
    
    # States
    'error': '#EF4444',          # Red
    'success': '#10B981',        # Green
    'warning': '#F59E0B'         # Yellow
}

FONTS = {
    'title': ('Segoe UI', 22, 'bold'),      # Larger title
    'subtitle': ('Segoe UI', 16, 'normal'),  # Subtitle
    'button': ('Segoe UI', 14, 'bold'),      # Buttons
    'entry': ('Segoe UI', 13, 'normal'),     # Input fields
    'label': ('Segoe UI', 14, 'bold'),     # Labels
    'small': ('Segoe UI', 12, 'normal')      # Small text
}

COMPONENT_CONFIG = {
    'entry_width': 260,
    'entry_height': 45,

    'btn_width': 160,

    'btn_search_with': 120,

    'btn_login_width': 260,
    'btn_login_height': 45,

    'small_entry_width': 140,
    'small_entry_height': 30
}

# Asset paths
ASSETS = {
    'cover_image': 'assets/cover.png',
    'banner': 'assets/banner.png'
}

# Temporary credentials (will be removed when backend is implemented)
TEMP_CREDENTIALS = {
    'username': 'admin',
    'password': 'admin123'
}

