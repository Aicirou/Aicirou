import datetime
import pytz
import random

def get_current_time_ist():
    utc_time = datetime.datetime.now(pytz.UTC)
    ist_time = utc_time.astimezone(pytz.timezone('Asia/Kolkata'))
    return ist_time.strftime('%Y-%m-%d %H:%M:%S IST')

def get_random_fortune():
    fortunes = [
        "The bug you're looking for is on line 42.",
        "Your code will compile on the first try today.",
        "A merge conflict-free day awaits you.",
        "The documentation will actually be helpful today.",
        "Your regex will work perfectly on the first attempt.",
        "A wild senior developer appears to answer your question.",
        "Your tests will pass without modification.",
        "The answer is not on Stack Overflow... just kidding, it is.",
    ]
    return random.choice(fortunes)

def generate_readme():
    template = f'''<div align="center">
  <img src="https://count.getloli.com/get/@Aicirou?theme=rule34" alt="Visitor Count" width="500">
</div>

<div align="center">
  
```
╔═══════════════════════════════════════════════════════════════════════════════╗
║                                                                               ║
║     █████╗ ██╗ ██████╗██╗██████╗  ██████╗ ██╗   ██╗                           ║
║    ██╔══██╗██║██╔════╝██║██╔══██╗██╔═══██╗██║   ██║                           ║
║    ███████║██║██║     ██║██████╔╝██║   ██║██║   ██║                           ║
║    ██╔══██║██║██║     ██║██╔══██╗██║   ██║██║   ██║                           ║
║    ██║  ██║██║╚██████╗██║██║  ██║╚██████╔╝╚██████╔╝                           ║
║    ╚═╝  ╚═╝╚═╝ ╚═════╝╚═╝╚═╝  ╚═╝ ╚═════╝  ╚═════╝                            ║
║                                                                               ║
║                    < code . create . contemplate >                            ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝
```

![Typing SVG](https://readme-typing-svg.herokuapp.com?font=JetBrains+Mono&size=14&duration=2000&pause=1000&color=00FF00&center=true&vCenter=true&random=false&width=500&lines=%24+./welcome.sh;Initializing+developer+profile...;%3E+Access+granted.+Welcome%2C+visitor.;while+(true)+%7B+learn();+create();+%7D)

</div>

---

<div align="center">

```
┌──────────────────────────────────────────────────────────────────────────────┐
│                           🐍 CONTRIBUTION SNAKE                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Aicirou/Aicirou/output/github-contribution-grid-snake-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/Aicirou/Aicirou/output/github-contribution-grid-snake.svg">
  <img alt="github contribution grid snake animation" src="https://raw.githubusercontent.com/Aicirou/Aicirou/output/github-contribution-grid-snake.svg">
</picture>

</div>

---

<details open>
<summary>💀 $ whoami</summary>

```text
┌─────────────────────────────────────────────────────────────────────────────┐
│ SYSTEM PROFILE                                                              │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  name        : Aicirou                                                      │
│  location    : 0.0.0.0:22                                                   │
│  timezone    : Asia/Kolkata (IST)                                           │
│  status      : ████████████████░░░░ 80% [debugging_life]                    │
│  coffee_level: ██████████░░░░░░░░░░ 50% [need_refill]                       │
│  mode        : [GODMODE ACTIVATED]                                          │
│                                                                             │
│  current_process:                                                           │
│    └── exploring_possibilities                                              │
│        └── building_dreams                                                  │
│            └── breaking_limits                                              │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

</details>

<details>
<summary>🔧 $ cat /etc/skills.conf</summary>

```ruby
# ═══════════════════════════════════════════════════════════════════════════
# SKILL CONFIGURATION FILE
# ═══════════════════════════════════════════════════════════════════════════

class Developer
  CONSTANTS = {{
    sleep_required: false,
    coffee_dependency: :critical,
    stackoverflow_visits_daily: Float::INFINITY
  }}
  
  def initialize
    @languages = {{
      primary:   [:python, :javascript, :go],
      exploring: [:rust, :zig],
      legacy:    [:java, :cpp]
    }}
    
    @tools = {{
      editor:    "neovim/vscode",
      shell:     "zsh + tmux",
      os:        "linux > *"
    }}
    
    @state = :perpetual_learning
    @mode  = :godmode
  end
  
  def daily_routine
    loop do
      code
      debug
      learn
      repeat
    end
  end
end
```

</details>

<details>
<summary>📊 $ htop --dev-stats</summary>

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ DEVELOPER STATISTICS                                                        │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ⚡ Commits      : [████████████████████] Loading from API...               │
│  🌙 Peak Hours   : 22:00 - 04:00 IST                                        │
│  🎯 Focus        : Building meaningful things                               │
│  🔥 Current Streak: Still going...                                          │
│                                                                             │
│  ┌─ PROCESSES ─────────────────────────────────────────────────────────┐   │
│  │ PID    PROCESS              CPU%    MEM%    STATUS                  │   │
│  │ 001    coding.exe           95%     80%     RUNNING                 │   │
│  │ 002    learning.daemon      100%    50%     ALWAYS_ON               │   │
│  │ 003    coffee.intake        ∞%      MAX     CRITICAL                │   │
│  │ 004    sleep.service        5%      10%     SUSPENDED               │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

</details>

<details>
<summary>🎰 $ fortune | cowsay</summary>

```
 _______________________________________ 
<  {get_random_fortune()}  >
 --------------------------------------- 
        \\   ^__^
         \\  (oo)\\_______
            (__)\\       )\\/\\
                ||----w |
                ||     ||
```

</details>

<br>

```shell
$ neofetch --github
```

<div align="center">
  <img src="/github-metrics.svg" alt="Metrics" width="500">
</div>

<br>

```shell
$ cat ~/.ssh/socials.pub
```

<div align="center">

[![Github](https://img.shields.io/badge/-Github-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Aicirou)
[![Gmail](https://img.shields.io/badge/-Gmail-EA4335?style=for-the-badge&logo=gmail&logoColor=white)](mailto:akm808.iitkgp@gmail.com)
[![LinkedIn](https://img.shields.io/badge/-LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/akm808-iitkgp)

</div>

---

<div align="center">

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                                                                             │
│  "In a world of code, be the exception that doesn't get caught."           │
│                                                                             │
│                                            - Anonymous Developer            │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

<sub>

```
╔══════════════════════════════════════════════════════════════════════════════╗
║  ⚙ Automated by GitHub Actions | 🕐 Last sync: {get_current_time_ist()}            ║
║  🔄 Profile updates daily | 🐍 Snake eats contributions continuously         ║
╚══════════════════════════════════════════════════════════════════════════════╝
```

</sub>

</div>'''
    return template

def main():
    readme_content = generate_readme()
    with open('README.md', 'w') as f:
        f.write(readme_content)

if __name__ == "__main__":
    main()

