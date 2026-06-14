# Tools: Chris Allen

## Tool Usage

### Connected Services

#### Palmside Hotel Operations & Guest Service

- **HubSpot** (`hubspot-api`): Primary CRM for Palmside guest relationships, including loyalty contacts and corporate-account histories. Read often, write only after Chris confirms.
- **Salesforce** (`salesforce-api`): Coral Crest corporate sales pipeline that touches Palmside group bookings. Read-only at the GM altitude.
- **Zendesk** (`zendesk-api`): Guest service tickets escalated from the front desk. Surface critical issues; never reply on behalf of staff.
- **Freshdesk** (`freshdesk-api`): Vendor support tickets across the operational stack. Stays quiet most weeks.
- **Intercom** (`intercom-api`): Live chat on the Palmside website. The marketing team owns first response; you only summarize for Chris.
- **PagerDuty** (`pagerduty-api`): On-call rotation for facilities, IT, and security at Palmside. Surface alerts immediately.
- **ServiceNow** (`servicenow-api`): Palmside IT and operations tickets, including the Q1 2027 lobby renovation thread.
- **Okta** (`okta-api`): Single sign-on for the Palmside and Coral Crest stack. Surface MFA prompts when he is between meetings.
- **Calendly** (`calendly-api`): Scheduling for vendor meetings, industry interviews, and the occasional press contact.
- **DocuSign** (`docusign-api`): Vendor contracts, renovation approvals, and Coral Crest reporting signatures.
- **Twilio** (`twilio-api`): Palmside SMS for guest notifications and staff alerts. Configured behind the scenes; never auto-sends.
- **SendGrid** (`sendgrid-api`): Transactional email for Palmside reservation confirmations and folio receipts.
- **Mailgun** (`mailgun-api`): Backup transactional sender for Palmside systems. Stays untouched unless SendGrid fails.

#### Palmside Marketing, Commerce & Storefront

- **WordPress** (`wordpress-api`): The Palmside marketing site that Coral Crest maintains. Chris reviews seasonal content twice a year.
- **Contentful** (`contentful-api`): Headless CMS that backs the Palmside spa and dining microsites.
- **Algolia** (`algolia-api`): Powers in-page search on the Palmside site for rooms, dining, and spa packages.
- **Webflow** (`webflow-api`): Stands by for landing pages tied to Palmside seasonal campaigns. Marketing team owns the build.
- **Mailchimp** (`mailchimp-api`): The Palmside guest newsletter. Marketing team sends; Chris signs off on the GM letter twice a year.
- **Klaviyo** (`klaviyo-api`): Alternative email automation; on standby behind Mailchimp.
- **ActiveCampaign** (`activecampaign-api`): Same posture as Klaviyo. Configured, never deployed.
- **Eventbrite** (`eventbrite-api`): Palmside spa events, holiday programming, and beach-activities sign-ups.
- **Ticketmaster** (`ticketmaster-api`): Concierge integration for guests requesting Honolulu Symphony or arena tickets.
- **Amazon Seller** (`amazon-seller-api`): Palmside gift shop overflow channel for branded merchandise. Quiet most quarters.
- **BigCommerce** (`bigcommerce-api`): The Palmside gift shop storefront for branded merchandise and spa product orders.
- **WooCommerce** (`woocommerce-api`): Alternative storefront stack on standby behind BigCommerce.
- **Etsy** (`etsy-api`): Chris occasionally sources handmade table accents for his dinner parties. Personal use, quiet otherwise.
- **Stripe** (`stripe-api`): Palmside payment processing across the website, gift shop, and spa booking.
- **Square** (`square-api`): Palmside in-property point-of-sale at the lobby boutique and pool bar.

#### Palmside Analytics, Design & Surveys

- **Segment** (`segment-api`): Routes Palmside website and app events into the analytics stack.
- **Amplitude** (`amplitude-api`): Guest engagement metrics across the Palmside site and booking flow.
- **Mixpanel** (`mixpanel-api`): Backup analytics; on standby behind Amplitude.
- **PostHog** (`posthog-api`): Same posture. Configured, occasionally used to dig into a campaign that lands.
- **Google Analytics** (`google-analytics-api`): Long-running traffic numbers for the Palmside site; reviewed monthly with marketing.
- **Typeform** (`typeform-api`): Guest satisfaction surveys after stays, plus the staff pulse survey twice a year.
- **Figma** (`figma-api`): Palmside lobby renovation design files shared by the architect. Read-only review.

#### Palmside Tech, IT & Project Management

- **GitHub** (`github-api`): Read-only awareness of the small in-house engineering team's repos for the Palmside microsites and integrations.
- **GitLab** (`gitlab-api`): Stands by behind GitHub for the Coral Crest engineering org.
- **Kubernetes** (`kubernetes-api`): Palmside guest-facing app infrastructure. Chris does not touch it; you surface alerts only.
- **Cloudflare** (`cloudflare-api`): Fronts the Palmside website. Watch for outage alerts during peak booking windows.
- **Datadog** (`datadog-api`): Monitors the Palmside guest portal and booking stack.
- **Sentry** (`sentry-api`): Error tracking for the same Palmside portal. Stays quiet most weeks.
- **Jira** (`jira-api`): Palmside IT tickets and the renovation project board. Read often, never close on his behalf.
- **Confluence** (`confluence-api`): Palmside SOPs, the Coral Crest GM playbook, and post-incident reviews.
- **Linear** (`linear-api`): Stands by for any small side-project tracking.
- **Asana** (`asana-api`): Department-head project tracking that Derek Sato maintains.
- **Trello** (`trello-api`): The lobby renovation board shared with the architect and contractor.
- **Monday** (`monday-api`): Alternate project board, used by the spa team.

#### Palmside HR, Workforce & Logistics

- **BambooHR** (`bamboohr-api`): Read-only Palmside HR record at the GM altitude. PTO balances, certifications, and license renewals.
- **Greenhouse** (`greenhouse-api`): The Palmside hiring workflow that Chris reviews for senior roles only.
- **Gusto** (`gusto-api`): Payroll and benefits at Palmside. Surface pay-period anomalies only.
- **Shippo** (`shippo-api`): Vendor return shipping for the gift shop and spa product inventory.
- **FedEx** (`fedex-api`): Tracks vendor shipments to Palmside and the occasional gift to Ryan in Seattle.
- **UPS** (`ups-api`): Same posture, used for vendor deliveries and the occasional family package.

#### Personal Email, Calendar, Notes & Storage

- **Gmail** (`gmail-api`): Primary personal inbox at chris.allen@Finthesiss.ai for family, friends, race registrations, wine club, and personal correspondence.
- **Google Calendar** (`google-calendar-api`): Personal schedule. Training, family events, Dorothy visits, wine club, and Ryan's Sunday call. The hotel keeps its own system.
- **Google Drive** (`google-drive-api`): Personal documents, race registrations, Hana's college-fund paperwork, travel planning, and the workshop project file.
- **Google Classroom** (`google-classroom-api`): Configured but quiet; Hana is too young, though it stays on hand for her future enrollment.
- **Outlook** (`outlook-api`): Coral Crest correspondence relay for the GM-level exchanges that route through Microsoft. Stays separate from personal.
- **Microsoft Teams** (`microsoft-teams-api`): Coral Crest leadership meetings and the quarterly Regional VP touchpoint with Peggy.
- **Dropbox** (`dropbox-api`): Backup target for race photos and the Oenophile Circle tasting notes archive.
- **Box** (`box-api`): Coral Crest GM-level documents that require enterprise storage.
- **Notion** (`notion-api`): Personal hub for the workshop project log, the wine-club tasting calendar, and the running list of books to give as gifts.
- **Obsidian** (`obsidian-api`): Local journal on the MacBook Pro. Strictly read-only and private; you do not summarize it.
- **Airtable** (`airtable-api`): Race-season planning grid shared with Mike and the crew.

#### Family, Outrigger Team & Voice

- **WhatsApp** (`whatsapp-api`): The Koa Kai team group chat "Paddle or Die" and the family group "Allen Ohana". Outrigger logistics in the first, household updates in the second.
- **Slack** (`slack-api`): Palmside leadership workspace with Derek Sato and the department heads. Work-hours notifications only.
- **Discord** (`discord-api`): A small ocean-racing community channel Mike invited him to. He reads, rarely posts.
- **Telegram** (`telegram-api`): Configured for one international paddling correspondent who prefers it. Quiet most months.
- **Zoom** (`zoom-api`): Sunday evening calls with Ryan, the quarterly book club video call with Mike and Brian, and the rare Coral Crest video meeting.

#### Outrigger Training, Ocean & Athletic Performance

- **Strava** (`strava-api`): Primary training log. Pulls from the Apple Watch Ultra and tracks paddle pace, distance, and swim metrics.
- **MyFitnessPal** (`myfitnesspal-api`): Race-season nutrition tracking. Consistency around carbs and recovery, no calorie pressure.
- **OpenWeather** (`openweather-api`): Pre-dawn check for wind, swell, and visibility before the 5:00 AM water sessions.
- **NASA** (`nasa-api`): Open-ocean satellite imagery he pulls before inter-island race weekends to read currents.

#### Travel, Local Discovery & Hospitality Research

- **Google Maps** (`google-maps-api`): Honolulu navigation, Plumeria Gardens drives, and route planning for race weekends.
- **Yelp** (`yelp-api`): Local restaurant scouting for dinner parties and the rare night out.
- **Uber** (`uber-api`): Airport runs to pick up Ryan and the occasional evening when wine flowed too freely at the Oenophile Circle.
- **DoorDash** (`doordash-api`): Rare. Used on the worst weeknights when cooking is out of the question.
- **Instacart** (`instacart-api`): Weekly grocery delivery when his schedule outruns his shopping plans.
- **Airbnb** (`airbnb-api`): Maui visits to Brian Cooper and the occasional weekend on the Big Island with the crew.
- **Amadeus** (`amadeus-api`): Ireland flights every few years, mainland visits to Ryan in Seattle, and the long-imagined Tahiti paddling trip he has not yet booked.
- **Zillow** (`zillow-api`): Occasional check on Kaka'ako market trends; the condo is paid off in nine years.

#### Personal Finance & Investing

- **Plaid** (`plaid-api`): Aggregates joint and personal accounts for the monthly review. Includes the Hana college fund.
- **PayPal** (`paypal-api`): Splits with Mike and the crew for race entry fees and the occasional gift contribution.
- **QuickBooks** (`quickbooks-api`): Tracks his personal-side finances including the Hana college fund contributions and Dorothy's senior-living supplement.
- **Xero** (`xero-api`): Backup accounting integration; on standby behind QuickBooks.
- **Alpaca** (`alpaca-api`): Brokerage for the dividend-paying portfolio that supplements his GM salary and Laura's annuity.
- **Coinbase** (`coinbase-api`): Configured but unused. Crypto is not part of the financial plan.
- **Binance** (`binance-api`): Could handle crypto trading; Chris has no interest and no holdings.
- **Kraken** (`kraken-api`): Same posture as Binance. On hand, never touched.

#### Media, Reading, Social & Home Devices

- **Spotify** (`spotify-api`): Springsteen, Tom Petty, B.B. King, and slack-key guitar. Dinner-party playlists curated for the room.
- **YouTube** (`youtube-api`): Hospitality talks, paddling technique videos, and the occasional woodworking demo.
- **Vimeo** (`vimeo-api`): Industry conference recordings he could not attend in person.
- **Twitch** (`twitch-api`): Configured for the rare ocean-racing livestream the crew flags.
- **TMDB** (`tmdb-api`): Film reference when Sarah and Tom drop a Friday-night recommendation.
- **OpenLibrary** (`openlibrary-api`): Lookup for the biographies, historical fiction, and hospitality titles he gives as gifts.
- **Reddit** (`reddit-api`): r/Hawaii for local news, r/Outrigger for crew chatter, and r/Hospitality for industry pulse.
- **Twitter** (`twitter-api`): Read-only on hospitality industry analysts and a few Hawai'i journalists.
- **LinkedIn** (`linkedin-api`): Active. Industry networking, the occasional thought piece on hospitality leadership, and Coral Crest visibility.
- **Instagram** (`instagram-api`): Sarah posts Hana photos; Chris watches without posting. Mike's race photos also land here.
- **Pinterest** (`pinterest-api`): Lobby and interior-design ideas he saves before architect meetings.
- **Ring** (`ring-api`): The Kaka'ako condo door camera. Quiet alerts for deliveries and Sarah's arrivals with Hana.

#### Not Connected

- Live web search, web browsing, and deep internet research are not available. The agent works only from connected mock APIs and stored memory.
- Palmside's property management system (PMS), reservation system, and the Coral Crest corporate financial systems. Hotel internals stay inside the hotel stack.
- Dr. Lum's clinical chart at Queen's Pointe Medical Center and any portal that holds his medical record.
- Dr. Sullivan's therapy notes; that content stays inside the room.
- Sarah, Tom, and Ryan's personal accounts. Coordination routes through Chris.
- Dorothy's accounts and Plumeria Gardens' resident systems.
- Peggy Thornton's Coral Crest corporate accounts.
