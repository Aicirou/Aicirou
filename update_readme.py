import datetime
import pytz
import os

def get_current_time():
    return datetime.datetime.now(pytz.UTC).strftime('%Y-%m-%d %H:%M:%S UTC')

def get_current_time_ist():
    utc_time = datetime.datetime.now(pytz.UTC)
    ist_time = utc_time.astimezone(pytz.timezone('Asia/Kolkata'))
    return ist_time.strftime('%Y-%m-%d %H:%M:%S IST')

def generate_readme():
    template = f'''<div align="left">
  <img src="/github-metrics.svg" alt="Metrics" width="400">
</div>

<div align="right">
  <img src="URL_TO_YOUR_LOLI_PICTURE" alt="Loli Picture" width="400">
</div>

<div align="center">

``ascii
              A I C I R O U
     < code . create . contemplate >
``

![Typing SVG](https://readme-typing-svg.herokuapp.com?font=JetBrains+Mono&size=12&duration=2000&pause=1000&color=777777&center=true&vCenter=true&random=false&width=435&lines=echo+%22Hello%2C+World%22;%2F%2F+Building+digital+dreams;%23+Exploring+the+unknown;while+(true)+%7B+learn();+%7D)

</div>

Last update: {get_current_time_ist()}
''' return template
def main():
readme_content = generate_readme()
with open('README.md', 'w') as f:
f.write(readme_content)

if name == "main":
main()

