# Dashboard Service
The **Dashboard Service** is an open **REST API integration** service within the Domain-Guard system, providing convenient endpoints for performing requests and obtaining unified outputs. It implements **user-centric** features such as *daily/regular domain data updates*, *browsing history searches*, and *advanced functionalities* for registered users. Additionally, it offers a free endpoint to gather domain DNS records (present and past) and lists of subdomains.


## Technology Stack
Built on Django and Django REST Framework (DRF).
Utilizes PyJWT for JWT **token cookie pair realization**, addressing security concerns.
Follows **Domain-Driven Design (DDD)** and **SOLID** principles, ensuring **core independence from Django or DRF**, **facilitating potential migration** to frameworks like Flask with minimal changes to the integration layer and repository ORM (e.g., replacing Django ORM with SQLAlchemy).


## Integration and Communication:
- Communicates with the Aggregator Service via **Remote Procedure Call (RPC)** to provide domain data.
- Uses **Redis** to store intermediate states of user registration processes.
- Implements email confirmation features using custom domain names via **MailerSend**.


## Development Status
#### Completed:
- Setup Project Structure.
- Implemented core features and functions.
- Implemented base repositories and services.
- Implemented login, logout, refresh views.

#### In Progress:
- User features (currently under development).
- Integration with the Aggregator Service.
- Enable advanced user features.
- Setup MongoDB for history data searches.


## Todo:
- include **Dockerfile** setup, **Docker-Compose** configuration for development environments.
- add multi-factor authentication **(MFA)**.
- add **CAPTCHA** registration validation.
- add integration with a** notification Telegram service**.