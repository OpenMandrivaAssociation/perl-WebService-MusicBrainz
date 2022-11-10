%define upstream_name    WebService-MusicBrainz
%define upstream_version 1.0.6

%{?perl_default_filter}

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    1

Summary:    Web service API to MusicBrainz database
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        https://search.cpan.org/dist/%{upstream_name}
Source0:    https://www.cpan.org/modules/by-module/WebService/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Mojolicious)
BuildArch:  noarch

%files
%doc Changes META.json META.yml MYMETA.yml
%{_mandir}/man3/*
%perl_vendorlib/*

#----------------------------------------------------------------------------

%description
This module will act as a factory using static methods to return specific
web service objects;

%prep
%autosetup -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build CFLAGS="%{optflags}"

%install
%make_install

