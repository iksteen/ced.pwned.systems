Title: for200 - Dropped Plates
Author: dsc
Date: 2016-06-03 15:12
Tags: CTF


**note:** This challenge is a continuation  of [for100](/hitb-2016-ctf-for100.html).

## Introduction

This is a write-up for the for200 challenge of the HiTB 2016 CTF.

> Some customers complained over the phone over not being able to access the Culinary Tour de Force's website.
> They got a strange message and couldn't make a reservation.

> We think the sever might be hacked, but we are not sure, we are chef's not investigators.
> You have access to this image <link> and our packet capture <link>.

> The attacker deleted some files and database information, are you able to reconstruct the deleted data?
> Note: !!!!Flagformat is not HITB but HITBCTF!!!!

> Could you check if his secrets are safe?

> Image file [here]({filename}/downloads/hitb-2016-ctf/ad30567ce980735e8c316f87b02e1235.img.xz). Pcap file [here]({filename}/downloads/hitb-2016-ctf/bin100/77590fce7ccc8a8b335bdcfb121e362a.pcap)

## Analysis

The description implies we need to look at the pcap and probably decrypt HTTPs traffic.

## Mounting

We mount the first disk label of the image:

	# slot 02: 64      * 512 = 32768
    # Slot 03: 2477952 * 512 = 1268711424
    # Slot 04: 8769408 * 512 = 4489936896

	mount -o ro,loop,offset=32768,ufstype=44bsd recipe.img mnt4

And we quickly find `etc/ssl/private/server.key`

	-----BEGIN RSA PRIVATE KEY-----
	MIICXQIBAAKBgQDPnaC4jVnI2iQ1CLoaDb5gKrRwprHxwjk9cIhPVSqC6XfKhY7a
	yq8UhQKIctNQoCvglgvMGuPJIu3admE+M5mg7dhnkyPGFzAMsLII63FONLp8ol6V
	idyIhVYv00hcbKZzuUUYvprx7cizO2+UFRFQkTRkgZJMND3L71w1knAlLwIDAQAB
	AoGAFUKH7b4TvpyP7ppZLEfSAdj9pzd6q03/PIpkevM2qjcsHCH3EfKFYS2Jp91S
	RERSmenjhWAPiU45WxCaPptcFM5jo3aNKBdeDP+uDSLdB5mNMDY6T7pY2Wl1+RyW
	iJZqR0zD4JknH7ocL+mcTBdgkrOjcx6OzgpGZBlAYiiewfkCQQDwxL87gB4rZEMO
	c/K9Da0QOtCYW8aqze5mjWC+E+2qfp2+0tanvhJSpSRL/qQ9y10TJJAdNPdgz/Yn
	B0aJRF2DAkEA3L/4XbgT7nX7ihgP0GPqvikDOcnRtQkxxzlRmSDbXOudGbg0ZMSn
	tnR3QRD42xnGUbEfHtOjcUMY0bxLbRRV5QJBAIQfs8F3IRc2wgWgY0iTxLDvVaEG
	XBNHRthIJRqp3PZ+3RnmoZ0TlQJ9VVnOt1qhysXCfsNIWahq9u2b9H1HYvkCQAou
	tLcl+Y1jVdH94CTdpwNUgviUbZ7rKKem5jOpB1VW7O01yPzo8U+COcn/jWsV2kcE
	Y4oZew2Lacaq59PFP10CQQCbXQSuzknEYWkAMEu2/3v9cS75fZAACbVpjODp4b1L
	M42fMv9WWvt380AgyJDfhha1DuAzX+pkROS9mF5vNuSP
	-----END RSA PRIVATE KEY-----

## Wireshark

Wireshark supports SSL decryption through the SSL dissector so in theory all we need to do is load our server.key into the dissector.

Start Wireshark and open `FOR200.pcap`.

`Edit -> Preferences -> Protocols -> SSL`

Specify SSL Debug File: `/tmp/lulz.debug`

Click 'RSA key list'. Click 'New'.

	Ip Address: 10.0.2.4 (The server using the certificate)
	Port: 443 (TCP port at the server side)
	Protocol: HTTP (the protocol carried inside the SSL/TLS session)
	File: [Pick 'etc/ssl/private/server.key' from the previously mounted disk'

And apply the changes.

If configured correctly, Wireshark has written the decrypted traffic to `/tmp/lulz.debug`. Lets grep through it:

	$ grep "HITBCTF{" /tmp/lulz.debug          
	<tr><td>qqzzqHITBCTF{FAKEFAKE}mjasej1mjasej1mjasejwhipped creamqbxqq</td><td></td>
	<td></td></tr><tr><td>qqzzqHITBCTF{FAKEFAKE2}mjasej10mjasej2mjasejprime ribqbxqq</td><td></td><td></td></tr>
	<tr><td>qqzzqHITBCTF{2d4a2238545194cdcd938f4a223ff203}mjasej1mjasej3mjasejfrikandellenqbxqq</td><td></td><td></td></tr>
	<tr><td>qqzzqHITBCTF{FAKEFAKE3}mjasej2mjasej4mjasejappeltaartqbxqq</td><td></td><td></td></tr></table></html>


And there we see the flag.

	HITBCTF{2d4a2238545194cdcd938f4a223ff203}