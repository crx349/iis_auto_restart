## iis-auto-restart

----

Windows下IIS自动监控并重启程序

----

### 功能

 Windows服务器下监控Cpu使用率，自动重启iis恢复网站运行，适用于Cpu比较弱（单核心）或站点短暂被攻击导致时cpu超过使用限额的状况下，iis自动重启恢复。

 py_iis.py 用途是监控CPU使用率重启IIS
 py_service_status.py 用途是检查IIS服务运行状态，在重启失败的情况下，自动恢复服务（理论上支持win下任意服务） 
 
### 开始使用

1. [安装Python3.7](https://www.python.org/downloads/windows/)
2.配置iis_re.bat和iis_st.bat python路径和py脚本路径
cd "C:\Program Files\Python37"
pythonw.exe D:\py\py_iis.py
3.Win计划任务添加 iis_re.bat和iis_st.bat执行 建议iis_re.bat每分钟1次 iis_st.bat没分钟2次




### License & Copyright
Copyright (c) 2014-2018 Beijing Duizhan Tech, Inc., All rights reserved.

Licensed under The GNU General Public License version 2 (GPLv2)  (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at

https://www.gnu.org/licenses/gpl-2.0.html

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.
