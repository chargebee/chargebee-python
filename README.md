= ChargeBee Python Client Library

The python library for integrating with ChargeBee Recurring Billing and Subscription Management solution.

== Installation

Install the latest version of the library with the following commands...

  $ pip install --upgrade chargebee
  
  or
  
  $ easy_install --upgrade chargebee

If you would prefer to install it from source...
  
  $ git clone git@github.com:chargebee/chargebee-python.git
  
  $ python setup.py install
  
== Documentation

For API reference see https://apidocs.chargebee.com/docs/api?lang=python

== Usage

To create a new subscription:
  
import chargebee
chargebee.configure(api_key, site)

res = chargebee.Subscription.create({
"plan_id" : "basic"
})

print res.subscription

== License

See the LICENSE file.

