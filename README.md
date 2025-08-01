# Cherry Blossom Terminal Animation

A minimalistic cherry blossom animation that plays when you open a new terminal window, featuring pink petals gliding across your screen. Pressing any button will proceed to normal terminal window. Works on macOS and Linux terminals.

![Demo](Demo.gif)

## Installation
       
1. Clone this repository, don't forget to change 'yourusername' to your actual github username:
   ```bash
   git clone https://github.com/yourusername/cherry-blossom-terminal.git
   cd cherry-blossom-terminal
   ```

2. Copy the script to your desired location:
   ```bash
   cp cherry_blossom.py ~/cherry_blossom.py
   ```

3. Add the animation to your shell startup file:

   **For Zsh (macOS default):**
   ```bash
   echo 'if [[ -t 1 && -z "$TMUX" && -z "$SSH_CLIENT" ]]; then' >> ~/.zshrc
   echo '    python3 ~/cherry_blossom.py' >> ~/.zshrc
   echo 'fi' >> ~/.zshrc
   ```

   **For Bash:**
   ```bash
   echo 'if [[ -t 1 && -z "$TMUX" && -z "$SSH_CLIENT" ]]; then' >> ~/.bashrc
   echo '    python3 ~/cherry_blossom.py' >> ~/.bashrc
   echo 'fi' >> ~/.bashrc
   ```

4. Restart your terminal or run:
   ```bash
   source ~/.zshrc  # or ~/.bashrc
   ```

## How it Works

The animation creates pink dots that fall from the top-right to bottom-left of your terminal. The script:

- Detects terminal size automatically
- Uses ANSI escape codes for positioning and colors
- Waits for any keypress before returning control to your shell
- Only runs in interactive terminals (not in scripts or SSH sessions)

You can modify the animation by editing `cherry_blossom.py`:

- **Petal color**: Change the `PINK` color code in the `Colors` class
- **Fall speed**: Adjust `speed_x` and `speed_y` values in the `PinkDot` class
- **Spawn rate**: Modify the frame check in the main loop 
- **Petal character**: Change the `char` property

## Requirements

- Python 3.x
- Unix-like terminal (macOS, Linux)
- Terminal that supports ANSI escape codes

## Uninstall

Remove the animation lines from your shell configuration file (`~/.zshrc` or `~/.bashrc`) and delete the script:

```bash
rm ~/cherry_blossom.py
```

## License

MIT License - feel free to modify and share!
