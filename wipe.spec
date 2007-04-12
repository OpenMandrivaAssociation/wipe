Name:           wipe
Version:        2.2.0
Release:        %mkrel 3
Epoch:          0
Summary:        Secure file deletion utility 
License:        GPL
Group:          File tools
URL:            http://wipe.sourceforge.net/
Source0:        http://unc.dl.sourceforge.net/sourceforge/%{name}/%{name}-%{version}.tar.bz2
Source1:        http://unc.dl.sourceforge.net/sourceforge/%{name}/%{name}-%{version}.tar.bz2.sig
Patch0:         %{name}-rootbuildfix.patch
Patch1:         %{name}-2.1.0-errno-fix.patch
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildRoot:      %{_tmppath}/%{name}-buildroot

%description
Wipe is a tool that effectively degauses the surface of a hard
disk, making it virtually impossible to retrieve the data that was
stored on it. This tool is designed to make sure secure data that is
erased from a hard drive is unrecoverable.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{configure2_5x}
%{make}

%install
%{__rm} -rf %{buildroot}
%{makeinstall}
%{__mv} %{buildroot}%{_bindir}/wipe %{buildroot}%{_bindir}/wipe.wipe
%{__mv} %{buildroot}%{_mandir}/man1/wipe.1 %{buildroot}%{_mandir}/man1/wipe.wipe.1

# remove package installed docs
rm -rf %{buildroot}/%{_datadir}/doc/%{name}

%clean
%{__rm} -rf %{buildroot}

%post
%{_sbindir}/update-alternatives --install %{_bindir}/wipe wipe %{_bindir}/wipe.wipe 10 --slave %{_mandir}/man1/wipe.1.bz2 wipe.1.bz2 %{_mandir}/man1/wipe.wipe.1.bz2

%postun
%{_sbindir}/update-alternatives --remove wipe %{_bindir}/wipe.wipe

%files
%defattr(0644,root,root,0755)
%doc LICENSE copyright README CHANGES TODO INSTALL TESTING
%attr(0755,root,root) %{_bindir}/wipe.wipe
%{_mandir}/man1/wipe.wipe.1*


