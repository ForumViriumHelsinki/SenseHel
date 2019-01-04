import React from 'react';
import { PullToRefresh as Pull } from 'react-js-pull-to-refresh';
import './pulltorefresh.styles.css';

const PullDownContent = () => <div className="pull-down-content" />;

const RefreshContent = () => (
  <div className="pull-down-content">
    <div className="lds-spinner">
      <div />
      <div />
      <div />
      <div />
      <div />
      <div />
      <div />
      <div />
      <div />
      <div />
      <div />
      <div />
    </div>
  </div>
);

const PullToRefresh = ({ onRefresh, children }) => (
  <Pull
    pullDownContent={<PullDownContent />}
    releaseContent={<PullDownContent />}
    refreshContent={<RefreshContent />}
    pullDownThreshold={150}
    triggerHeight="100%"
    onRefresh={onRefresh}
    backgroundColor="white"
  >
    {children}
  </Pull>
);

export default PullToRefresh;
