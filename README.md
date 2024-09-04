<!-- Name & Banner -->
<p align="center">
    <img src="https://socialify.git.ci/smile-jefferson/Python_Multiple-Processes/image?description=0&font=Source%20Code%20Pro&forks=1&issues=1&language=1&name=1&owner=1&pattern=Solid&pulls=1&stargazers=1&theme=Auto" alt="smile-jefferson" width="640" height="320" />
    <a href="https://git.io/typing-svg"><img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=800&size=24&duration=2000&pause=2000&center=true&vCenter=true&width=450&height=60&lines=HI+there!+I'm+Jefferson!;I'm+a+full-stack+enginer;Hope+you+guys+like+my+page" alt="Typing SVG" /></a>
</p>

<!-- Index 索引 
    # Visitor
        # https://visitor-badge.laobi.icu/
        * https://visitorbadge.io/
        來源: https://github.com/pudding0503/github-badge-collection/blob/main/README.md#31-%E8%AE%BF%E9%97%AE%E9%87%8F
-->
## Table of contents <a href="https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2FAnmol-Baranwal%2FAnmol-Baranwal"><img src="https://api.visitorbadge.io/api/visitors?path=https://github.com/smile-jefferson/Python_Multiple-Processes&label=Repo%20Views&countColor=%23ff8a65&style=plastic&labelStyle=none" /></a>
<a href="https://github.com/smile-jefferson/Python_Multiple-Processes">
    <picture>
        <source media="(prefers-color-scheme: dark)" srcset="https://user-images.githubusercontent.com/74038190/212750147-854a394f-fee9-4080-9770-78a4b7ece53f.gif">
        <img height="175px" align='right' src="https://github.com/Anmol-Baranwal/Cool-GIFs-For-GitHub/assets/74038190/219bcc70-f5dc-466b-9a60-29653d8e8433" >
    </picture>
</a>

- [Project](#project)
- [Side Project](#side-project-)
- [Github Status](#my-status--language-)
- [Github Trophy](#my-trophy-)
- [Github Streak](#my-streak-)



<!-- 當下專案內容 -->
## Project👋💻

<!-- 專案開始日期 -->
<img alt="Static Badge" src="https://img.shields.io/badge/Start_Date-2024_%2F_09_%2F_04-FFD43B?style=plastic&logo=Python&logoColor=%23FFD43B&label=Start%20Date&color=blue">

<!-- 專案使用技術 Badge 版本A。 來源:https://shields.io/-->
![Python](https://img.shields.io/badge/Python-%23306998.svg?style=plastic&logo=Python&logoColor=%23FFD43B)

Python的多進程同步方式 :
* multiple processing
在使用 Python 的 `multiprocessing` 模塊進行多進程編程時，有幾種常見的同步方式來保證多進程之間的協調和數據一致性。以下是一些主要的同步方式：

### 1. `Lock`

`Lock` 是最基本的同步原語，它用於確保只有一個進程可以在任何時候執行特定的代碼區塊。

```python
import multiprocessing

lock = multiprocessing.Lock()

def critical_section():
    with lock:
        # 這裡的代碼在同一時刻只能由一個進程執行
        pass
```

### 2. `RLock` (可重入鎖)

`RLock` 是一種可以被同一進程多次獲得的鎖。它適用於在一個進程中重複需要獲得鎖的情況。

```python
import multiprocessing

rlock = multiprocessing.RLock()

def critical_section():
    with rlock:
        # 這裡的代碼在同一時刻只能由一個進程執行
        pass
```

### 3. `Semaphore`

`Semaphore` 用於限制同時進程的數量。它可以設置一個初始計數值，表示允許多少個進程同時執行某段代碼。

```python
import multiprocessing

sem = multiprocessing.Semaphore(2)  # 允許最多兩個進程同時執行

def critical_section():
    with sem:
        # 這裡的代碼最多由兩個進程同時執行
        pass
```

### 4. `Event`

`Event` 用於進程之間的信號傳遞。當一個進程設置事件時，其他等待這個事件的進程會被通知。

```python
import multiprocessing
import time

event = multiprocessing.Event()

def worker():
    event.wait()  # 等待事件被設置
    print("Event received!")

def trigger_event():
    time.sleep(2)
    event.set()  # 設置事件，通知所有等待的進程

if __name__ == '__main__':
    p1 = multiprocessing.Process(target=worker)
    p2 = multiprocessing.Process(target=trigger_event)
    
    p1.start()
    p2.start()
    
    p1.join()
    p2.join()
```

### 5. `Condition`

`Condition` 用於進程之間的複雜同步和通信。它允許進程在某些條件滿足時進行協作。

```python
import multiprocessing

condition = multiprocessing.Condition()

def worker():
    with condition:
        # 等待條件變為真
        condition.wait()
        print("Condition met!")

def signal_condition():
    with condition:
        # 設置條件並通知所有等待的進程
        condition.notify_all()

if __name__ == '__main__':
    p1 = multiprocessing.Process(target=worker)
    p2 = multiprocessing.Process(target=signal_condition)
    
    p1.start()
    p2.start()
    
    p1.join()
    p2.join()
```

### 6. `Manager`

`Manager` 可以用來創建進程間共享的數據結構，如列表、字典等。這些共享的數據結構可以在多個進程間進行讀寫操作。

```python
import multiprocessing

def worker(d, key, value):
    d[key] = value

if __name__ == '__main__':
    with multiprocessing.Manager() as manager:
        shared_dict = manager.dict()
        
        p1 = multiprocessing.Process(target=worker, args=(shared_dict, 'a', 1))
        p2 = multiprocessing.Process(target=worker, args=(shared_dict, 'b', 2))
        
        p1.start()
        p2.start()
        
        p1.join()
        p2.join()
        
        print(shared_dict)  # 輸出: {'a': 1, 'b': 2}
```

### 7. `Value` 和 `Array`

`Value` 和 `Array` 用於創建共享的數據對象，這些對象可以被多個進程讀寫。這些數據對象通常需要使用鎖來確保數據的一致性。

```python
import multiprocessing
import time

def increment(counter, lock):
    for _ in range(100):
        with lock:
            counter.value += 1
        time.sleep(0.01)

if __name__ == '__main__':
    counter = multiprocessing.Value('i', 0)
    lock = multiprocessing.Lock()
    
    p1 = multiprocessing.Process(target=increment, args=(counter, lock))
    p2 = multiprocessing.Process(target=increment, args=(counter, lock))
    
    p1.start()
    p2.start()
    
    p1.join()
    p2.join()
    
    print(f"Final counter value: {counter.value}")
```

### 總結

- **`Lock` 和 `RLock`** 用於基本的互斥和鎖定。
- **`Semaphore`** 用於控制進程的並發數量。
- **`Event` 和 `Condition`** 用於進程之間的通知和條件同步。
- **`Manager`** 提供了進程間共享的數據結構。
- **`Value` 和 `Array`** 用於進程間共享基本數據。

根據你的需求選擇適合的同步方式，可以有效地管理多進程之間的協作與數據一致性。



- [back to top](#table-of-contents)
---

<!-- 延伸專案
    寫法A: ![Customized Card](https://github-readme-stats.vercel.app/api/pin?username=smile-jefferson\&repo=TEST&title_color=f0f0f0&icon_color=9f9f9f&text_color=f9f9f9&bg_color=515151)
    來源: https://github.com/anuraghazra/github-readme-stats/blob/master/readme.md

    [![Readme Card](https://github-readme-stats.vercel.app/api/pin/?username=anuraghazra&repo=github-readme-stats)](https://github.com/anuraghazra/github-readme-stats)
-->
## Side Project 👨‍💻
<img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Wrench.png" alt="Wrench" width="25" height="25" />
<a href="https://github.com/smile-jefferson/Python_Multiple-Processes">
    <picture>
        <source media="(prefers-color-scheme: dark)" srcset="https://github-readme-stats.vercel.app/api/pin?username=smile-jefferson&repo=Python_Multiple-Processes&title_color=f0f0f0&icon_color=9f9f9f&text_color=f9f9f9&bg_color=515151">
        <img alt="Shows smile-jefferson's GitHub Stats." src="https://github-readme-stats.vercel.app/api/pin?username=smile-jefferson&repo=Python_Multiple-Processes&theme=default">
    </picture>
</a>

<!-- Spotify 
    # 來源: https://github.com/magic-ike/spotify-data-card?tab=readme-ov-file#examples
-->
## What I'm Listening
<a href="https://data-card-for-spotify.herokuapp.com/card?user_id=smie.jefferson05">
  <img background="#00000000" src="https://data-card-for-spotify.herokuapp.com/api/card?user_id=smie.jefferson05" alt="Data Card for Spotify">
</a>

<!-- Activity 
    # 來源: https://ashutosh00710.github.io/github-readme-activity-graph/
-->
## My Activity 👣
<a href="https://github.com/smile-jefferson/Python_Multiple-Processes" width="50%">
    <picture>
        <source media="(prefers-color-scheme: dark)" srcset="https://github-readme-activity-graph.vercel.app/graph?username=smile-jefferson&bg_color=000000&color=ffffff&line=147500&point=00ff04&area=true&hide_border=true">
        <img width="100%" alt="Shows smile-jefferson's GitHub Stats." src="https://github-readme-activity-graph.vercel.app/graph?username=smile-jefferson&theme=github-light">
    </picture>
</a>

<!-- Status & Language 
    # 來源: https://github.com/anuraghazra/github-readme-stats
-->
## My Status & Language 👟
<a href="https://github.com/smile-jefferson/TEST">
    <a href="https://github.com/smile-jefferson/Python_Multiple-Processes">
        <picture>
            <source media="(prefers-color-scheme: dark)" srcset="https://github-readme-stats.vercel.app/api?username=Jefferson&show_icons=true&theme=radical">
            <img width="51%" alt="Shows smile-jefferson's GitHub Stats." src="https://github-readme-stats.vercel.app/api?username=Jefferson&show_icons=true&theme=compact">
        </picture>
    </a>
    <a href="https://github.com/smile-jefferson/Python_Multiple-Processes">
        <picture>
            <source media="(prefers-color-scheme: dark)" srcset="https://github-readme-stats-eight-theta.vercel.app/api/top-langs/?username=Jefferson&theme=dark&layout=compact&langs_count=6">
            <img width="45.25%" alt="Shows smile-jefferson's GitHub Stats." src="https://github-readme-stats-eight-theta.vercel.app/api/top-langs/?username=Jefferson&theme=transparent&layout=compact&langs_count=6">
        </picture>
    </a>
</a>

<!-- Trophy
    # 來源: https://github.com/ryo-ma/github-profile-trophy?tab=readme-ov-file#matrix
-->
## My Trophy 🏆
<a href="https://github.com/smile-jefferson/Python_Multiple-Processes">
    <picture>
        <source media="(prefers-color-scheme: dark)" srcset="https://github-profile-trophy.vercel.app/?username=smile-jefferson&theme=onedark">
        <img alt="Shows smile-jefferson's GitHub Stats." src="https://github-profile-trophy.vercel.app/?username=smile-jefferson&theme=flat">
    </picture>
</a>


<!-- Streak
    # 來源: https://github.com/DenverCoder1/github-readme-streak-stats/blob/main/docs/themes.md
-->
## My Streak 🔎
<a href="https://github.com/smile-jefferson/Python_Multiple-Processes">
    <picture>
        <source media="(prefers-color-scheme: dark)" srcset="https://github-readme-streak-stats.herokuapp.com/?user=smile-jefferson&theme=dark&count_private=true&bg_color=0d1116&title_color=ce09ec&text_color=a4aacb&icon_color=007ec6">
        <img alt="Shows smile-jefferson's GitHub Stats." src="https://github-readme-streak-stats.herokuapp.com/?user=smile-jefferson&theme=blood&count_private=true">
    </picture>
</a>