#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-String-Approx
Version  : 3.28
Release  : 6
URL      : https://cpan.metacpan.org/authors/id/J/JH/JHI/String-Approx-3.28.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/J/JH/JHI/String-Approx-3.28.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libs/libstring-approx-perl/libstring-approx-perl_3.28-1.debian.tar.xz
Summary  : unknown
Group    : Development/Tools
License  : Artistic-2.0 GPL-2.0 LGPL-2.1 MIT
Requires: perl-String-Approx-lib = %{version}-%{release}
Requires: perl-String-Approx-license = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
Welcome to String::Approx 3.0.
This release is a major update from String Approx 2,
of which 2.7 was the last release.  See later about the future
of version 2.

%package dev
Summary: dev components for the perl-String-Approx package.
Group: Development
Requires: perl-String-Approx-lib = %{version}-%{release}
Provides: perl-String-Approx-devel = %{version}-%{release}

%description dev
dev components for the perl-String-Approx package.


%package lib
Summary: lib components for the perl-String-Approx package.
Group: Libraries
Requires: perl-String-Approx-license = %{version}-%{release}

%description lib
lib components for the perl-String-Approx package.


%package license
Summary: license components for the perl-String-Approx package.
Group: Default

%description license
license components for the perl-String-Approx package.


%prep
%setup -q -n String-Approx-3.28
cd ..
%setup -q -T -D -n String-Approx-3.28 -b 1
mkdir -p deblicense/
mv %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/String-Approx-3.28/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-String-Approx
cp COPYRIGHT %{buildroot}/usr/share/package-licenses/perl-String-Approx/COPYRIGHT
cp deblicense/copyright %{buildroot}/usr/share/package-licenses/perl-String-Approx/deblicense_copyright
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.1/x86_64-linux-thread-multi/String/Approx.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/String::Approx.3

%files lib
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.1/x86_64-linux-thread-multi/auto/String/Approx/Approx.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-String-Approx/COPYRIGHT
/usr/share/package-licenses/perl-String-Approx/deblicense_copyright
