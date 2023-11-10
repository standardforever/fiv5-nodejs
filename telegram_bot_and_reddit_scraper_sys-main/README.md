# telegram_bot_and_reddit_scraper_sys

# INSTALLING AND RUNING THIS REPO

# Build and Test
`docker build -t rdan-telegram-and-reddit-bot .`


# Running
`docker run rdan-telegram-and-reddit-bot`


[JSON2TABLE](http://json2table.com/#)

- client/id?: WcRkVk7z-cQwYLhAKNjaWQ
- secret: cib6QCNBQ4N2EpH7h7jNQ0B9aMEcIw
- name: rdan_agg
- redirect uri: http://www.example.com/unused/redirect/uri

https://www.reddit.com/dev/api/oauth#GET_api_mod_conversations_subreddits
some redd

## *modhashes*
A modhash is a token that the reddit API requires to
help prevent CSRF. Modhashes can be obtained via the
/api/me.json call or in response data of listing endpoints.
The preferred way to send a modhash is to include an
X-Modhash custom HTTP header with your requests.

For legacy reasons, all JSON response bodies currently
have <, >, and & replaced with &lt;, &gt;, and &amp;,
respectively. If you wish to opt out of this behaviour,
add a raw_json=1 parameter to your request.

- GET /api/v1/meidentity
  - Returns the identity of the user.

- GET /r/subreddit/about/traffic


My Subreddits mysubreddits
Access the list of subreddits I moderate, contribute to, and subscribe to.

- GET /api/v1/me/friends/usernamemysubreddits
  - Get information about a specific 'friend', such as notes.
    - id  |  A valid, existing reddit username

- GET /subreddits/mine/where	mysubredditsrss  |  support
 /subreddits/mine/subscriber
 /subreddits/mine/contributor
 /subreddits/mine/moderator
 /subreddits/mine/streams
---

- GET /api/v1/scopesany
  - Retrieve descriptions of reddit's OAuth2 scopes.
  If no scopes are given, information on all scopes are returned.
  Invalid scope(s) will result in a 400 error with body that indicates the invalid scope(s).

---

# _Scopes_

> scopes  |  (optional) An OAuth2 scope string

Many default User-Agents (like "Python/urllib" or "Java") are
drastically limited to encourage unique and descriptive
user-agent strings.

Defines the permissions the web app needs, to function
properly. A list of a couple of these scopes along with
their descriptions is:
- account:  Update preferences and related account information.
Will not have access to your email or password.
- identify: Access my reddit username and signup date.
- read: Access posts and comments through my account.
- my_subreddits: Access list of subreddits I mod,contrib. to &/or subscribe to.
    - `id`=my_subreddits  |  name=`My Subreddits`
- subscribe: Manage my subreddit subscriptions. Manage "friends" - users whose content I follow.


---




Get subreddits the user has a relationship with.
The where parameter chooses which subreddits are returned as follows:

- subscriber:  subreddits the user is subscribed to
- contributor: subreddits the user is an approved user in
- moderator:  subreddits the user is a moderator of
- streams:  subscribed to subreddits that contain hosted video links


- GET /subreddits/mine/where	mysubredditsrss  |  support /subreddits/mine/subscriber /subreddits/mine/contributor /subreddits/mine/moderator /subreddits/mine/streams


- after  |  fullname of a thing
- before  |  fullname of a thing
- count  |  a positive integer (default: 0)
- limit  |  the maximum number of items desired (default: 25, maximum: 100)
- show  |  (optional) the string all
- sr_detail  |  (optional) expand subreddits

???
> This endpoint is a listing.   

???


## Reddit JSON API Response Result Data Structure

Used to paginate content that is too long to display in one go.
Add the query argument before or after with the value given to
get the previous or next page. This is usually used in conjunction
with a count argument.

Exception: Unlike the other classes documented on this page, `Listing`
is not a thing subclass, as it inherits directly from the Python base
class, `Object`. Although it does have data and kind as parameters, it
does not have id and name. A listing's kind will always be Listing
and its data will be a List of things.

### `Listing` Fields Description

`type`-`name`-`description`

- String - before - The fullname of the listing that follows before this page. null if there is no previous page.
- String - after - The fullname of the listing that follows after this page. null if there is no next page.
- String - modhash - This modhash is not the same modhash provided upon login. You do not need to update your user's modhash everytime you get a new modhash. You can reuse the modhash given upon login.
- List<thing> - children - A list of things that this Listing wraps.


### [`subreddit` Fields Description](https://github.com/reddit-archive/reddit/wiki/JSON#subreddit)


`type`-`name`-`description`


- String - url - The relative URL of the subreddit. Ex: "/r/pics/"
	- For e.g. https://www.reddit.com/r/datascience/ + top/ => https://www.reddit.com/r/datascience/top/

