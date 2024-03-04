# Use the official PHP 8.0 image as base
FROM php:8.0-cli

# Set working directory
WORKDIR /app

# Install dependencies
RUN apt-get update && apt-get install -y \
    git \
    zip \
    unzip

# Install Composer
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer
