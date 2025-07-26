#!/usr/bin/env python3
import time
import os
import random
import sys
import select
import termios
import tty

class Colors:
    RESET = '\033[0m'
    PINK = '\033[38;5;218m'  # Soft pink cherry blossom color
    WHITE = '\033[97m'
    GRAY = '\033[90m'

def clear_screen():
    print('\033[2J\033[H', end='')

def move_cursor(x, y):
    print(f'\033[{y};{x}H', end='')

def hide_cursor():
    print('\033[?25l', end='')

def show_cursor():
    print('\033[?25h', end='')

def draw_samurai(rows):
    samurai = [
        "    ⚔️",
        "   /|\\",
        "    |",
        "   / \\",
        "  /   \\",
        "   | |",
        "   | |"
    ]
    
    start_y = max(1, rows - len(samurai) - 2)
    
    for i, line in enumerate(samurai):
        move_cursor(3, start_y + i)
        if i == 0:  # Sword
            print(f"{Colors.WHITE}{line}{Colors.RESET}", end='')
        else:  # Body
            print(f"{Colors.GRAY}{line}{Colors.RESET}", end='')
    
    # Add ground
    move_cursor(1, rows - 1)
    print(f"{Colors.GRAY}{'─' * 15}{Colors.RESET}", end='')

class PinkDot:
    def __init__(self, cols, rows):
        # Start from top-right area, avoid samurai area
        self.x = random.randint(cols - 20, cols)
        self.y = random.randint(1, 5)
        self.speed_x = random.uniform(-2.0, -1.0)  # Move left (more horizontal)
        self.speed_y = random.uniform(0.4, 1.0)    # Move down (slower)
        self.char = '●'
        self.color = Colors.PINK
        
    def update(self):
        self.x += self.speed_x
        self.y += self.speed_y
        
    def is_visible(self, cols, rows):
        return 1 <= self.x <= cols and 1 <= self.y <= rows
        
    def draw(self):
        if self.x >= 1 and self.y >= 1:
            move_cursor(int(self.x), int(self.y))
            print(f"{self.color}{self.char}{Colors.RESET}", end='')

def kbhit():
    """Check if a key has been pressed"""
    if not sys.stdin.isatty():
        return False
    return select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], [])

def pink_dots_animation():
    # Check if we're in a proper terminal
    if not sys.stdin.isatty():
        return
        
    try:
        cols, rows = os.get_terminal_size()
    except:
        cols, rows = 80, 24
    
    dots = []
    clear_screen()
    hide_cursor()
    
    # Set terminal to raw mode for immediate key detection
    try:
        old_settings = termios.tcgetattr(sys.stdin)
        tty.setraw(sys.stdin.fileno())
    except:
        return
    
    
    try:
        frame = 0
        while True:
            # Check for keypress
            if kbhit():
                sys.stdin.read(1)  # Read the key
                break
            
            # Clear screen but preserve instruction
            for i in range(1, rows - 3):
                move_cursor(1, i)
                print(' ' * cols, end='')
            
            # Add new dots periodically
            if frame % 3 == 0:
                dots.append(PinkDot(cols, rows - 4))
            
            # Update and draw all dots
            dots_to_keep = []
            for dot in dots:
                dot.update()
                if dot.is_visible(cols, rows - 4):
                    dot.draw()
                    dots_to_keep.append(dot)
            
            dots = dots_to_keep
            
            
            sys.stdout.flush()
            time.sleep(0.1)
            frame += 1
            
    except KeyboardInterrupt:
        pass
    finally:
        # Restore terminal settings
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)
        clear_screen()
        show_cursor()

if __name__ == "__main__":
    try:
        pink_dots_animation()
    except Exception as e:
        show_cursor()
        clear_screen()
        print(f"Error: {e}")