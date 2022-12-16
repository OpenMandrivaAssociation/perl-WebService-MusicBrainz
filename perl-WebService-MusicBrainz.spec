%define debug_package %{nil}

%define oname    WebService-MusicBrainz

%{?perl_default_filter}

Summary:    Web service API to MusicBrainz database
Name:       perl-%{oname}
Version:    1.0.6
Release:    1
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        https://search.cpan.org/dist/%{oname}
Source0:    https://www.cpan.org/modules/by-module/WebService/%{oname}-%{version}.tar.gz

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
%autosetup -n %{oname}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build CFLAGS="%{optflags}"

%install
%make_install

