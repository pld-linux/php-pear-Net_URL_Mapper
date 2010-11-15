%include	/usr/lib/rpm/macros.php
%define		_status		beta
%define		_pearname	Net_URL_Mapper
Summary:	%{_pearname} - a simple and flexible way to build nice URLs for web applications
Summary(pl.UTF_8):	%{_pearname} - prosty i elastyczny sposób tworzenia ładnie wyglądających URL-i dla aplikacji WWW
Name:		php-pear-%{_pearname}
Version:	0.9.1
Release:	1
License:	New BSD License
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	0d27b8d5a6a3e38b310807f2fcee996f
URL:		http://pear.php.net/package/Net_URL_Mapper/
BuildRequires:	php-pear-PEAR >= 1:1.4.3
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
Requires:	php-pear-Net_URL >= 1.0.14
Requires:	php-pear-PEAR-core >= 1:1.4.3
Obsoletes:	php-pear-Net_URL_Mapper-tests
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Net_URL_Mapper provides a simple and flexible way to build nice URLs
for your web applications.

The URL syntax is similar to what can be found in Ruby on Rails or
Python Routes module and as such, this package can be compared to what
they call a router.

Still, Net_URL_Mapper does not perform the dispatching like these
frameworks and therefore can be used with your own router.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF_8
Net_URL_Mapper udostępnia prosty i elastyczny sposób tworzenia ładnie
wyglądających adresów URL dla aplikacji WWW.

Składnia URL-a jest zbliżona do tej jaką można spotkać w Ruby on Rails
czy module Routes języka Python i w związku z tym pakiet ten może być
porównany z tym co nazywane jest tam routerem.

Mimo to, w odróżnieniu od wspomnianych frameworków, Net_URL_Mapper nie
zajmuje się przekazywaniem zapytań i w związku z tym może być użyty
wraz z osobnym routerem.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

# tests should not be packaged
%{__rm} -r $RPM_BUILD_ROOT%{php_pear_dir}/tests/%{_pearname}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%dir %{php_pear_dir}/Net/URL
%{php_pear_dir}/Net/URL/Mapper
%{php_pear_dir}/Net/URL/Mapper.php

%{php_pear_dir}/data/%{_pearname}
