Name: 		perl-Regexp-Common
Version: 	2010010201
Release: 	2%{?dist}
Summary: 	Regexp::Common Perl module
# Old Artistic 1.0 is also valid, but we won't list it here since it is non-free.
# Also, it would throw off the automated license check and flag this package.
License: 	Artistic 2.0 or MIT or BSD
Group: 		Development/Libraries
URL: 		http://search.cpan.org/dist/Regexp-Common/
Source0: 	http://www.cpan.org/authors/id/A/AB/ABIGAIL/Regexp-Common-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch: noarch
BuildRequires:  perl(ExtUtils::MakeMaker)

# for improved tests
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)

Requires:  	perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
Regexp::Common - Provide commonly requested regular expressions

%prep
%setup -q -n Regexp-Common-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type d -depth -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*

%clean
rm -rf $RPM_BUILD_ROOT

%check
make test

%files
%defattr(-,root,root,-)
%doc TODO README
%{perl_vendorlib}/Regexp
%{_mandir}/man3/*

%changelog
* Thu May 06 2010 Marcela Maslanova <mmaslano@redhat.com> - 2010010201-2
- Mass rebuild with perl-5.12.0

* Mon Mar 08 2010 Ralf Corsépius - 2010010201-1
- Upstream update.

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 2.122-4
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.122-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.122-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu May 29 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 2.122-1
- update to 2.122
- license change

* Wed Mar  5 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 2.120-7
- rebuild for new perl

* Wed Aug 29 2007 Ralf Corsépius <rc040203@freenet.de> - 2.120-6
- BR: perl(ExtUtils::MakeMaker).

* Tue Sep 05 2006 Ralf Corsépius <rc040203@freenet.de> - 2.120-5
- Mass rebuild.

* Sat Feb 25 2006 Ralf Corsépius <rc040203@freenet.de> - 2.120-4
- Rebuild for FC5/perl-5.8.8.

* Thu Aug 20 2005 Ralf Corsepius <ralf@links2linux.de> - 2.120-3
- Further spec cleanup.

* Thu Aug 20 2005 Ralf Corsepius <ralf@links2linux.de> - 2.120-2
- Spec cleanup.

* Thu Aug 11 2005 Ralf Corsepius <ralf@links2linux.de> - 2.120-1
- FE submission.
