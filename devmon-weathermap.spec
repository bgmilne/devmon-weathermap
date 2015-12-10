%{?!hobbit:%global hobbit xymon}

#Arch is not noarch, since hobbit home dir is arch-dependant :-(

Name: devmon-weathermap
Version: 1.1.5
Source: %{name}-%{version}.tar.gz
License: GPL
Group: Monitoring
Summary: Network Weather Map for Devmon and Hobbit/Xymon
Release: %mkrel 1
Requires: %{hobbit}
Requires: optipng
BuildRoot: %{_tmppath}/%{name}-root

%description
Network Weather Map for Devmon / Hobbit

%prep
%setup -q

%build

%install
rm -Rf %{buildroot}
mkdir -p %{buildroot}/{%{_sysconfdir}/%{hobbit}/hobbitlaunch.d,%{_libdir}/%{hobbit}/server/ext,/var/lib/%{hobbit}/www/weathermap/images/{white,black},%{_datadir}/%{hobbit}/www/help/}

install -m 755 weathermap %{buildroot}/%{_libdir}/%{hobbit}/server/ext/weathermap.pl
install -m 644 weathermap.conf %{buildroot}/%{_sysconfdir}/%{hobbit}/weathermap/
install -m 644 weathermap.cfg %{buildroot}/%{_sysconfdir}/%{hobbit}/hobbitlaunch.d/
install -m 644 overlib_mini.js %{buildroot}/var/lib/%{hobbit}/www/weathermap
install -m 644 LiberationMono-Regular.ttf %{buildroot}/%{_sysconfdir}/%{hobbit}/weathermap
install -m 644 images/white/*.png %{buildroot}/var/lib/%{hobbit}/www/weathermap/images/white
install -m 644 images/black/*.png %{buildroot}/var/lib/%{hobbit}/www/weathermap/images/black
install -m644 weathermap.html %{buildroot}/%{_datadir}/%{hobbit}/www/help/

%files
%defattr(-,root,root)
%dir %{_sysconfdir}/%{hobbit}/weathermap
%config(noreplace) %{_sysconfdir}/%{hobbit}/weathermap/*.conf
%config(noreplace) %{_sysconfdir}/%{hobbit}/hobbitlaunch.d/weathermap.cfg
%{_sysconfdir}/%{hobbit}/weathermap/*.ttf
/var/lib/%{hobbit}/www/weathermap/images
%{_libdir}/%{hobbit}/server/ext/weathermap.pl
/var/lib/%{hobbit}/www/weathermap/overlib_mini.js
%{_datadir}/%{hobbit}/www/help/weathermap.html
