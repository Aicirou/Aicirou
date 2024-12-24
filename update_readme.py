import datetime
import pytz
import os

# def get_current_time():
#     return datetime.datetime.now(pytz.UTC).strftime('%Y-%m-%d %H:%M:%S UTC')

def get_current_time_ist():
    utc_time = datetime.datetime.now(pytz.UTC)
    ist_time = utc_time.astimezone(pytz.timezone('Asia/Kolkata'))
    return ist_time.strftime('%Y-%m-%d %H:%M:%S IST')

def generate_readme():
    template = f'''<div align="center">
  <img src="https://count.getloli.com/get/@Aicirou?theme=rule34" alt="Loli Picture" width="500">
</div>

<div align="center">
  
```ascii
            A I C I R O U
     < code . create . contemplate >
```

![Typing SVG](https://readme-typing-svg.herokuapp.com?font=JetBrains+Mono&size=12&duration=2000&pause=1000&color=777777&center=true&vCenter=true&random=false&width=435&lines=echo+%22Hello%2C+World%22;%2F%2F+Building+digital+dreams;%23+Exploring+the+unknown;while+(true)+%7B+learn();+%7D)

</div>

---

<details open>
<summary>$ whoami</summary>

```yaml
name: Aicirou
location: /earth/somewhere
timezone: UTC
status: debugging_life
current_task: exploring_possibilities
```

</details>

<details>
<summary>$ cat skills.log</summary>

```ruby
class Developer
  def initialize
    @languages = [:javascript, :python, :go]
    @state = :learning
    @mode = :godmode:
  end
end
```

</details>

<details>
<summary>$ uptime</summary>

```shell
⚡ Commits: Loading...
🌙 Active: Usually after sunset
🎯 Focus: Building meaningful things
```

</details>

<br>

```shell
$ git stats --brief
```

<div align="center">
  <img src="/github-metrics.svg" alt="Metrics" width="500">
</div>

```shell
$ contact --all
```

<div align="center">
  
[![Github](https://img.shields.io/badge/-Github-black?style=flat&logo=github)](https://github.com/Aicirou)
[![Mail](https://img.shields.io/badge/-Mail-black?style=flat&logo=gmail)](mailto:akm808.iitkgp@gmail.com)
[![LinkedIn](https://img.shields.io/badge/-LinkedIn-black?style=flat&logo=linkedin)](https://linkedin.com/in/akm808-iitkgp)

</div>

```shell
$ echo "Don't follow the path. Create your own."
```

---

<div align="right">
<sub>Last update:{get_current_time_ist()}</sub>
</div>'''
    return template
def main():
    readme_content = generate_readme()
    with open('README.md', 'w') as f:
    f.write(readme_content)
if name == "main":
main()
