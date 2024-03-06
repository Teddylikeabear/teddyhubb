# Use the official PHP 8 image from Docker Hub
FROM php:8.0

# Set the working directory in the container
WORKDIR /var/www/html

# Copy the current directory contents into the container at /var/www/html
COPY . /var/www/html

# Install any dependencies your PHP application might need
# For example, if you're using Composer for PHP dependency management, you can install it like this:
RUN apt-get update && \
    apt-get install -y \
    git \
    zip \
    && \
    curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer

# Install PHP extensions if needed (you can add more extensions as per your requirements)
RUN docker-php-ext-install pdo_mysql

# Expose port 80 to the Docker host, so you can access your application from the outside
EXPOSE 80

# Start the PHP built-in server (you can adjust this command based on your project's needs)
CMD ["php", "-S", "0.0.0.0:80"]
