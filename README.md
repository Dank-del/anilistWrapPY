<!--
 * This file is part of anilistWrapPY (https://github.com/Dank-del/anilistWrapPY).
 * Copyright (c) 2021 Sayan Biswas, ALiwoto.
-->

# <img src="https://avatars.githubusercontent.com/u/18018524?s=200&v=4" width="35px" align="left"></img> anilistWrapPY
> Name:		anilistWrapPY	\
> Version:	v0.0.14				\
> Edit:		1 Aug 2021			\
> By:		Dank-del (Sayan Biswas) (C)	

-----------------------------------------------------------

![downloads](https://img.shields.io/pypi/dm/anilistWrapPY) ![ver](https://img.shields.io/pypi/v/anilistWrapPY)

anilistWrapPY is an unofficial [python](https://python.org) wrapper for [anilist](https://anilist.co) API.

### Table of contents:

 * [Supported python versions](#supported-python-versions)
 * [Features](#features)
 * [Getting started](#getting-started)
 * [How to use](#how-to-use)
 * [Support and Contributions](#support-and-contributions)
 * [Helpful Links](#links)
 * [License](#license)


<img src="https://raw.githubusercontent.com/aliwoto/aliwoto/main/resources/798246901916499998.gif" width="350px"></img>

<hr/>


## Supported python versions

This library, needs python 3.7 or higher version to be installed.

<hr/>

## Features

- Uses official anilist API endpoints, which makes this library:
   - Easy to update
   - Guaranteed to match the docs
   - No third party endpoints
   - No need to serialize and deserialize data outside of library
- It's in pure python, no need to install any kind of plugin or include any kind of additional files.
- It uses GraphQL to fetch data on AniList servers. The AniList GraphQL API provides quick and powerful access to over 500k anime and manga entries, including character, staff, and live airing data.
- Anilist Client: Using a client makes it easier to fetch every type of data you want from the servers. You only need to import client and you are ready to go!

<hr/>

## Getting started

You can easily download the library with the standard `pip install` command:

```bash
pip install anilistWrapPY
```

You may want to visit our pypi page [here](https://pypi.org/project/anilistwrappy/).

<hr/>

## How to use


 - <img src="https://raw.githubusercontent.com/aliwoto/aliwoto/main/resources/soulgem-homura.gif" width="15px"></img> [Airing](#Airing)
 - <img src="https://raw.githubusercontent.com/aliwoto/aliwoto/main/resources/soulgem-kyoko.gif" width="15px"></img> [Anime](#Anime)
 - <img src="https://raw.githubusercontent.com/aliwoto/aliwoto/main/resources/soulgem-madoka.gif" width="15px"></img> [Character](#Character)
 - <img src="https://raw.githubusercontent.com/aliwoto/aliwoto/main/resources/soulgem-mami.gif" width="15px"></img> [Manga](#Manga)
 - <img src="https://raw.githubusercontent.com/aliwoto/aliwoto/main/resources/soulgem-sayaka.gif" width="15px"></img> [Media](#Media)
 - <img src="https://raw.githubusercontent.com/aliwoto/aliwoto/main/resources/Yayyyyyyyyy.png" width="15px"></img> [User](#User)


### Airing:

```py
>>> from anilistWrapPY import aniWrapPYClient
>>> c = aniWrapPYClient()
>>> c.Airing("The Detective Is Already Dead")
```

### Anime

```py
>>> from anilistWrapPY import aniWrapPYClient
>>> c = aniWrapPYClient()
>>> c.Anime("Kanojo mo kanojo")
```

### Character

```py
>>> from anilistWrapPY import aniWrapPYClient
>>> c = aniWrapPYClient()
>>> c.Character("Rin tohsaka")
```

### Manga

```py
>>> from anilistWrapPY import aniWrapPYClient
>>> c = aniWrapPYClient()
>>> c.Manga("Classroom of the elite")
```

### Media

```py
>>> from anilistWrapPY import aniWrapPYClient
>>> c = aniWrapPYClient()
>>> c.Media("Talentless Nana")
```

### User

```py
>>> from anilistWrapPY import aniWrapPYClient
>>> c = aniWrapPYClient()
>>> c.User("mimiee")
```


<hr/>


## Support and Contributions

 * If you think you have found a bug or have a feature request, feel free to use our [issue tracker](https://github.com/Dank-del/anilistWrapPY/issues). Before opening a new issue, please search to see if your problem has already been reported or not.  Try to be as detailed as possible in your issue reports.

 * If you need help using AniList APIs or have other questions about this library, we suggest you to join our [telegram community](https://t.me/chiruzon).  Please do not use the GitHub issue tracker for personal support requests.

 * Having a problem with library? Wanna talk with repository's owner? Contact the [Maintainer](https://t.me/dank_as_fuck)!

 * Want to have a cool multi-purpose Telegram bot in your groups? You can add [Nana[ナナ]](https://t.me/TheTalentlessBot) with full features of AniList API!


 


<hr/>

## Links

 * [Official website](https://anilist.co)
 * [AniList github org](https://github.com/AniList)
 * [AniList GraphQL docs](https://github.com/AniList/ApiV2-GraphQL-Docs)
 * [Support chat](https://t.me/chiruzon)
 * [Maintainer's Telegram](https://t.me/dank_as_fuck)
 * [Nana [ナナ]](https://t.me/TheTalentlessBot)

<hr/>

## License

<img src="https://raw.githubusercontent.com/aliwoto/aliwoto/main/resources/Something_that_looks_like_Diamond.png" width="25px"></img> The anilistWrapPY project is under the [Unlicense](http://unlicense.org/). You can find the license file [here](LICENSE).
