# What happens when you type google.com in your browser and press ENTER

To properly answer this question, one must first understand the underlisted concepts.
```bash
- DNS request
- Web server
- TCP/IP
- Firewall
- HTTPS/SSL
- Load-balancer
- Application server
- Database
```

Okay, so the above might seem like a lot or complicated but I assure you, it's pretty easy or at least I'll try to make it seem that way.

Let's get one thing clear, the web doesn't understand what `google.com` is literally, rather it tries to make sense of it through what is called `DNS`. DNS which stands for Domain Name system can simply be thought of as an address book that stores names and IP addresses (that is the weird numbers you know, e.g. 8.8.8.8 or 192.168.0.1). IP addresses are unique, just like your home address. No two public server can have the same IP address. (server, a term that will later be defined)

Now that we understand what `DNS` means and it's role, we can now dive deep into understanding how the web works.

The web is simply an interconnected network of computers, sending requests and receiving responses. Let's use this opportunity to define some terminology, we can think of `Client` as a computer that sends a request and a `Server` as one that receives the request and sends out a response to the Client. Let's link this to an example, consider Person A who orders pizza from Company B, Person A can be thought of as the Client and Company B as the server. But how does the `Client` know how to contact the `Server`? that's where `DNS` comes in.

Whenever a Client wants to send a request (e.g to google.com), the client's Browser first searches for the name google.com in DNS to get the corresponding IP address.

```sh
** Example DNS Table **
google.com | 8.8.8.8
facebook   | 157.240.192.0
Instagram  | 163.70.128.174
```

when it's found, then the request is sent to the server with the IP address. Here comes another question, how is the request transported? That's right, you have one minute to think about it. Alright, I'm sure you guessed `TCP/IP` which is correct. 

`TCP/IP` stands for Transmission Control Protocol/Internet Protocol. TCP/IP is a set of standardized rules that allow computers to communicate on a network such as the internet.
IP is the part that obtains the address to which data is sent. TCP is responsible for data delivery once that IP address has been found. Back to our example, when Person A orders pizza from Company B, it can only do that by having the address of Company B, could be a Physical or contact address (`IP Address`) but the ordering part was either via a phone call, instructing someone to go place the order at the physical location, the means is called the (`TCP`). So, we understand that IP/TCP are seperate concepts, so why do we use them together always, it's simple, because individually they aren't useful.

_Now, we understand what happens when you type google.com in your browser and hit enter. Wait do we really understand it all? Well for the most part we understand, however, there are other high level concepts that ensure google.com is rendered when we hit enter._

**Honestly, you can stop here, you've come a long way but if you're like me and simply can't get enough by all means forge ahead.**

## Other Important Concepts.

Let's talk more about Servers, earlier we said a `Server` is a computer (on steriods) that receives the request and sends out a response to the Client.
Servers host our application and returns it to the Client when requested for. Let's take an example, I'd like you to visit a website I built for a client, a few years ago [indicelsolar](http://indicelsolar.com/). You would notice that the website returns a static (not changing) page. Servers that serve static content like `indicelsolar` are called `Web Servers`. While servers that serve dynamic (changing) content/page are called `Application Servers`.

Application Servers primarily enable interaction between end-user clients and server-side application code (or business logic) — to generate and deliver dynamic content, such as transaction results (e.g. Bank Apps), decision support, or real-time analytics.

_By strict definition, a web server is a subset of an application server._

Oh yes, we are getting somewhere. Now, take a guess, is google.com an application server or a web server (I'd like to hear your answer in the comment).

A really important concept I'd like to talk about is HTTP, HTTPS/SSL. Let's start with HTTP - HyperText Transfer Protocol.
- HyperText refers to documents or files (text, images, graphics or videos)
- Transfer refers to the idea that files can move over the World Wide Web
- Protocol refers to set of computer rules that govern how devices are able to use the Internet

`HTTP` is built on top of the `TCP/IP` network protocol suite and on top of other layers in the protocol stack. Specifically, HTTP is an application layer protocol and is the primary protocol used for communication and data transfer between a web client and a web server.

I know, a lot of computer jargons, the main idea to take is that HTTP is a communication protocol for `Client` and `Servers`.

Now whenever you see `http://<some url>` you know what `http` means. But wait, I see `https` more often, are they the same? The simple answer is almost, except that https means HyperText Transfer Protocol Secure. You can think of it as the secure version of http.

So how does https work? Each data packet sent over an HTTPS connection is encrypted and secure, using cryptographic protocols such as TLS or SSL, on top of HTTP. Transport Layer Security (TLS), formely known as Secure Sockets Layer (SSL), is the protocol used to encrypt communications. It is the newer and more secure version of SSL.

HTTPS provides authentication for users and data, making sure transactions are kept private without fearing a data breach during the client-server communication. Most large companies like google, facebook, redhat, amazon all communicate via https.

The front desk officer / receptionist is super important in any large organisation. They perform the important task of redirecting you to the appropriate person or room. When a website needs to scale, more servers are usually added but adding more servers without having a means to redirect the traffic appropraitely is a waste. This is where your front desk officer comes in, but in software engineering such systems are called `Load balancers`. Load balancers redirect traffic to servers to improve server-client response time.

`Firewalls` are set of rules placed to either enable or deny access to a particular resource. Have you ever visited a website, only to find out you cannot access it unless you turn on your VPN, there's a firewall rule not allowing your location to access the website. Sometimes a certain piece of information may be made only for a specific audience and one major way to guard it from the public is to set rules / establish a Firewall.

Creating an Account, Making a Post, Liking or commenting on a video or post, sharing images via the web. All these transactions would not be possible without a `Database,` be it a simple file storage or a sophisticated database storage like MySQL, PostgreSQL, Google clouds, Amazon Redshift. Database are the warehouse of our applications, they store contents either in raw format or encrypted formats (like user passwords).

## RECAP
*User A types `google.com` and hits enter: User A's Browser searches for the `IP address` of google.com in `DNS`. google.com being a large system has thousands of servers, therefore to manage that, it makes use of a `Load Balancer` to redirect traffic to it's many `Servers`. It's safe to say that the IP address attached to google.com is the IP address of it's Load Balancer. Communication via the `Client` and the `Servers` of google.com is done via `HTTPS` a secure version of `HTTP`, which relies on `TLS or SSL` handshake. Once communication is established the requested content is sent to the User's browser, in this case the fancy google.com page you see.*

## CONCLUSION
To wrap up, a series of sequence is initiated when you type google.com in your web browser and hit enter. (Now you know it all).
