%define upstream_name    MooseX-ConfigFromFile
%define upstream_version 0.13

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1

Summary:	An abstract Moose role for setting attributes from a configfile

License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/MooseX/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires: perl(Test::Without::Module)
BuildRequires: perl(Test::Requires)
BuildRequires: perl(Test::Deep)
BuildRequires: perl(MooseX::Types::Path::Tiny)
BuildRequires:	perl(Moose)
BuildRequires:	perl(MooseX::Types::Path::Class)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test::Fatal)
BuildRequires:	perl(namespace::autoclean)
Requires:	perl(namespace::autoclean)
BuildArch:	noarch

%description
This is an abstract role which provides an alternate constructor for
creating objects using parameters passed in from a configuration file. The
actual implementation of reading the configuration file is left to concrete
subroles.

It declares an attribute 'configfile' and a class method 'new_with_config',
and requires that concrete roles derived from it implement the class method
'get_config_from_file'.

Attributes specified directly as arguments to 'new_with_config' supercede
those in the configfile.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc ChangeLog README
%{_mandir}/man3/*
%{perl_vendorlib}/*


