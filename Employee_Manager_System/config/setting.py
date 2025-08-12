"""
Global application settings
"""

# Window settings
WINDOW_CONFIG = {
    'width': 1000,  # Increased for better proportion
    'height': 600,  # Increased for better proportion
    'title': 'Employee Management System - Login',
    'resizable': False
}

COLORS = {
    # Main colors
    'primary': '#3B82F6',       # Modern blue
    'primary_hover': '#2563EB', # Hover blue
    'secondary': '#F8FAFC',     # Very light gray
    'accent': '#10B981',        # Green for success
    
    # Text colors
    'text_primary': '#1E293B',   # Dark gray
    'text_secondary': '#64748B', # Medium gray
    'text_light': '#FFFFFF',     # White
    
    # Background colors
    'bg_primary': '#FFFFFF',     # White
    'bg_secondary': '#F1F5F9',   # Light gray
    'bg_card': '#FFFFFF',        # White for cards
    
    # Border colors
    'border_light': '#E2E8F0',   # Light border
    'border_focus': '#3B82F6',   # Focus border
    
    # States
    'error': '#EF4444',          # Red
    'success': '#10B981',        # Green
    'warning': '#F59E0B'         # Yellow
}

FONTS = {
    'title': ('Segoe UI', 28, 'bold'),      # Larger title
    'subtitle': ('Segoe UI', 16, 'normal'),  # Subtitle
    'button': ('Segoe UI', 14, 'bold'),      # Buttons
    'entry': ('Segoe UI', 13, 'normal'),     # Input fields
    'label': ('Segoe UI', 12, 'normal'),     # Labels
    'small': ('Segoe UI', 10, 'normal')      # Small text
}

COMPONENT_CONFIG = {
    'entry_width': 280,
    'entry_height': 45,
    'button_width': 280,
    'button_height': 45,
    'card_padding': 40,
    'border_radius': 12
}

# Asset paths
ASSETS = {
    'cover_image': 'assets/cover.png',
    'logo': 'assets/logo.png'
}

# Temporary credentials (will be removed when backend is implemented)
TEMP_CREDENTIALS = {
    'username': 'admin',
    'password': 'admin123'
}
