Summary:	Clear location button next to the location bar.
Name:		mozilla-addon-diggler
%define		_realname	diggler
Version:	0.1
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://diggler.mozdev.org/%{_realname}-%{version}.xpi
Source1:	%{_realname}-installed-chrome.txt
URL:		http://diggler.mozdev.org/
BuildRequires:	unzip
BuildArch:	noarch
Requires:	mozilla >= 1.0-7
BuildRoot:	%{tmpdir}/%{_realname}-%{version}-root-%(id -u -n)

%define         _prefix         /usr/X11R6
%define         _chromedir      %{_libdir}/mozilla/chrome

%description
Diggler is a simple add-on to the navigator functionality in Mozilla. It
adds a clear location button next to the location bar much like the one in
Konqueror. It also has a drop down menu with some more useful actions such
as being able to navigate to parent directories in URLs. This feature is
especially handy for FTP operations.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_chromedir}

unzip %{SOURCE0} -d $RPM_BUILD_ROOT%{_chromedir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_chromedir}

%post
cat %{_chromedir}/*-installed-chrome.txt >%{_chromedir}/installed-chrome.txt

%postun
cat %{_chromedir}/*-installed-chrome.txt >%{_chromedir}/installed-chrome.txt

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_chromedir}/%{_realname}.jar
%{_chromedir}/%{_realname}-installed-chrome.txt
