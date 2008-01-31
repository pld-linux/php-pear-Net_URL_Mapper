%include	/usr/lib/rpm/macros.php
%define		_class		Net
%define		_subclass	URL_Mapper
%define		_status		beta
%define		_pearname	Net_URL_Mapper
Summary:	%{_pearname} - Provides a simple and flexible way to build nice URLs for web applications
Summary(pl.UTF_8):	%{_pearname} - dostarcza prostego i elastycznego sposobu do tworzenia ładnie wyglądających URLi dla aplikacji web
Name:		php-pear-%{_pearname}
Version:	0.9.0
Release:	4
License:	New BSD License
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	11a4d002f881ac5d957cdbb6b46139f7
URL:		http://pear.php.net/package/Net_URL_Mapper/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
Requires:	php-pear-Net_URL >= 1.0.14
Requires:	php-pear-PEAR >= 1.4.3
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
Net_URL_Mapper dostarcza prostego i elastycznego sposobu do tworzenia
ładnie wyglądających adresów URL dla aplikacji web.

Składnia URL jest zbliżona do tej jaką można spotkać w Ruby on Rails
czy module Routes języka Python i w związku z tym pakiet ten może być
porównany z tym co nazywane jest tam routerem.

Mimo to, w odróżnieniu od wspomnianych frameworków Net_URL_Mapper nie
robi zajmuje się przekazywaniem zapytań i w związku z tym może być
użyty wraz z Twoim routerem.

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl):	Testy dla PEAR::%{_pearname}
Group:		Development/Languages/PHP
AutoReq:	no
Requires:	%{name} = %{version}-%{release}
AutoProv:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl
Testy dla PEAR::%{_pearname}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%dir %{php_pear_dir}/Net/URL
%{php_pear_dir}/Net/URL/Mapper
%{php_pear_dir}/Net/URL/Mapper.php

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/Net_URL_Mapper
