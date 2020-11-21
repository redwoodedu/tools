# Dynamic-QR

Make QR code dynamically using Github Issues Comments

## Quick Start

1. Fork this repo and set the forked repo with Github pages
2. Create a `config.json` under the forked repo (take the `config_sample.json` as an example)
3. Create a issue, could be under any repo
4. Put the issue comments API (e.g. `https://api.github.com/repos/NoahDragon/Dynamic-QR/issues/1/comments`) into the `config.json` `url` fields
5. Create QR based on the URL `https://[URL to the github repo page]?dest=[name config in config.json]`
6. Comment in the created issue in step 3 will update the redirect URL

## Config File Format

Please take `config_sample.json` as example. Customized fields are in `[]`.

```
{
	["dest_name"]: {
		"url": ["Github issue comments link"],
		"author": ["empty if anyone can update the redirect url, set to a user then only the user's comments can affect the redirect"]
	}
}
```

## Limits

* Github Pages have [10 mins cache](https://webapps.stackexchange.com/questions/44871/caching-assets-in-github-pages-github-io) for all htmls, so need to clean caches if commented in issue within 10 mins.
* If the comment contains multiple URL, only the first one will be taken.